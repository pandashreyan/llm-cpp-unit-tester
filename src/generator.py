import os
import subprocess
import re

import requests  # Requires requests package

SRC_PATH = os.path.join('src', 'main.cpp')
TEST_PATH = os.path.join('test', 'test_main.cpp')
BUILD_DIR = 'build'


LLM_PROMPT = """
Given the following C++ code, generate Google Test unit tests that cover all logic.
At the top of the test file, add #include \"../src/main.cpp\" so the tests can access the functions.
Do NOT generate a main() function in the test file.
Do NOT call the application's main() function from the tests.
If only main() exists, test the output of the program by capturing std::cout.
Do NOT use std::get, std::tuple, or std::array unless they are present in the provided code. Only use functions and types that are actually defined in the code.
Output ONLY valid C++ code for the test file, with NO explanations, NO comments, and NO markdown formatting.
{code}
"""


REFINE_PROMPT = """
Given the following C++ code and test code, and the feedback below (build errors, test failures, or coverage issues), refine the test code to fix issues and improve coverage.
At the top of the test file, add #include \"../src/main.cpp\" so the tests can access the functions.
Do NOT generate a main() function in the test file.
Do NOT call the application's main() function from the tests.
If only main() exists, test the output of the program by capturing std::cout.
Do NOT use std::get, std::tuple, or std::array unless they are present in the provided code. Only use functions and types that are actually defined in the code.
Output ONLY valid C++ code for the test file, with NO explanations, NO comments, and NO markdown formatting.

Code:
{code}

Current Test Code:
{test_code}

Feedback:
{feedback}
"""

def extract_cpp_code(text):
    # Extract code between ``` or ```cpp blocks, or return the whole text if not found
    match = re.search(r"```(?:cpp)?\n(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text.strip()

# Fix unbalanced braces in generated C++ code
def fix_unbalanced_braces(code):
    open_braces = code.count('{')
    close_braces = code.count('}')
    if open_braces > close_braces:
        code += '\n' + ('}' * (open_braces - close_braces))
    elif close_braces > open_braces:
        # Remove only from the end, not from the middle
        extra = close_braces - open_braces
        for _ in range(extra):
            idx = code.rstrip().rfind('}')
            if idx != -1:
                code = code[:idx] + code[idx+1:]
    return code

def call_llm(prompt):
    # Call Ollama's local API using the /api/generate endpoint
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3",  # Change to your preferred model name
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    data = response.json()
    if 'response' in data:
        return data['response']
    else:
        raise RuntimeError("Unexpected Ollama response format: {}".format(data))

def write_test_file(test_code):
    with open(TEST_PATH, 'w') as f:
        f.write(test_code)

def build_and_run_tests():
    os.makedirs(BUILD_DIR, exist_ok=True)
    subprocess.run(['cmake', '..'], cwd=BUILD_DIR, check=True)
    build = subprocess.run(['cmake', '--build', '.'], cwd=BUILD_DIR, capture_output=True, text=True)
    if build.returncode != 0:
        return False, build.stderr
    test = subprocess.run(['ctest', '--output-on-failure'], cwd=BUILD_DIR, capture_output=True, text=True)
    return test.returncode == 0, test.stdout + test.stderr

def ensure_gtest_main(test_code):
    # If no main() present, append a minimal Google Test main (always correct)
    if 'int main(' not in test_code:
        main_code = '''
int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
'''
        return test_code + '\n' + main_code
    # Also fix any LLM mistakes (e.g., InitGoogle instead of InitGoogleTest)
    test_code = test_code.replace('InitGoogle(&argc, argv)', 'InitGoogleTest(&argc, argv)')
    return test_code

def strip_main_function(code):
    # Remove any function that looks like int main(...) { ... }
    # This regex is greedy and will remove the whole main function, even if not followed by a newline
    return re.sub(r'int\s+main\s*\([^)]*\)\s*\{[\s\S]*?\}', '', code, flags=re.MULTILINE)

def contains_forbidden_cpp(code, allowed):
    # Only allow std::get, std::tuple, std::array if present in allowed
    forbidden = ["std::get", "std::tuple", "std::array"]
    for word in forbidden:
        if word in code and word not in allowed:
            return True
    return False

def main():
    with open(SRC_PATH) as f:
        code = f.read()
    feedback = None
    code_no_main = strip_main_function(code)
    allowed = code_no_main  # Only allow LLM to use what is in the code
    for _ in range(5):
        test_code = call_llm(LLM_PROMPT.format(code=code_no_main))
        test_code = extract_cpp_code(test_code)
        test_code = fix_unbalanced_braces(test_code)
        test_code = strip_main_function(test_code)  # <--- NEW: Remove any main() from generated test code
        test_code = ensure_gtest_main(test_code)
        # Check for forbidden C++ features
        if contains_forbidden_cpp(test_code, allowed):
            print("LLM generated forbidden C++ features, refining...")
            feedback = "Do not use std::get, std::tuple, or std::array."
            continue
        write_test_file(test_code)
        success, output = build_and_run_tests()
        if success:
            print("Tests passed!\n", output)
            break
        else:
            print("Refining tests based on feedback...\n", output)
            test_code = call_llm(REFINE_PROMPT.format(code=code_no_main, test_code=test_code, feedback=output))
            test_code = extract_cpp_code(test_code)
            test_code = fix_unbalanced_braces(test_code)
            test_code = strip_main_function(test_code)  # <--- NEW: Remove any main() from generated test code
            test_code = ensure_gtest_main(test_code)
            if contains_forbidden_cpp(test_code, allowed):
                print("LLM generated forbidden C++ features, refining...")
                feedback = "Do not use std::get, std::tuple, or std::array."
                continue
    else:
        print("Failed to generate passing tests after 5 iterations.")

if __name__ == "__main__":
    main()
