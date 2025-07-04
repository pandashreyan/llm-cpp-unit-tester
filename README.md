# 🚀 LLM-powered C++ Unit Test Generator

✨ **Automatically generate high-quality unit tests for your C++ projects using AI** ✨

## 🔍 Project Overview
This innovative tool leverages Large Language Models to:
- 🧠 Intelligently analyze C++ source code
- ⚡ Generate comprehensive unit tests automatically
- 🔄 Continuously refine tests through feedback loops
- 📊 Achieve high code coverage with minimal effort

## 🛠️ Key Features
✅ **Smart Code Analysis** - Understands your code structure deeply
✅ **AI-Powered Generation** - Creates human-like test cases
✅ **Iterative Refinement** - Improves tests based on execution feedback
✅ **Seamless Integration** - Works with CMake and Google Test
✅ **Coverage Tracking** - Visualizes test coverage metrics

## 🚀 Getting Started
### Prerequisites
- Python 3.x
- CMake
- C++ compiler
- Google Test
- LLM API access (e.g., OpenAI)

### Installation
```bash
git clone https://github.com/your-repo/llm-cpp-tester.git
cd llm-cpp-tester
pip install -r requirements.txt
```
### Usage
1. Place your C++ source files in src/
2. Run the generator:
```
python src/generator.py
```
3. Build and run tests:
```
mkdir build && cd build
cmake .. && make
./run_tests
```
## 📊 Current Stats
Metric Value Tests Passing 168/168 ✅ Functions.cpp Coverage 81.82% Test Coverage 100%

## ✅ Test & Coverage Summary

| 🧩 **Metric**              | 🔢 **Value**   |
|---------------------------|----------------|
| ✅ Tests Passing           | 168 / 168      |
| 📄 Functions.cpp Coverage  | 81.82%         |
| 🧪 Total Test Coverage     | 100%           |

---



---    
 
## 🤝 Contributing
We welcome contributions! Please see our Contribution Guidelines .

## 📜 License
MIT License - see LICENSE for details.

## Project Goal
To develop a tool that automatically generates and refines unit tests for C++ applications using a Large Language Model (LLM).

## Tool Description
This tool automates the generation and refinement of unit tests for C++ code using a large language model (LLM). It follows an iterative workflow:

1. Analyze C++ source code.
2. Generate initial unit tests using an LLM.
3. Build and run the tests, collecting feedback (build errors, test failures, coverage).
4. Refine tests based on feedback.
5. Repeat until tests pass and coverage is satisfactory.
## Architecture Overview
### Components:
1. Code Analyzer : Parses C++ source code to extract functions, classes, and dependencies.
2. LLM Interface : Communicates with the LLM to generate test cases.
3. Test Generator : Formulates prompts for the LLM based on code analysis.
4. Build System Integrator : Manages compilation of generated tests.
5. Test Runner : Executes the generated unit tests.
6. Feedback Loop : Analyzes test results for iterative improvement.
7. Coverage Analyzer : Measures test coverage.
## Files
- src/analysis.cpp : Source code analysis utilities
- src/generator.py : Python script to orchestrate workflow
- src/functions.cpp : Example implementation (81.82% coverage)
- test/test_main.cpp : Generated tests (100% coverage)
- test/generation_instructions.yaml : Prompt for generating tests
- test/refinement_instructions.yaml : Prompt for refining tests
