# Unit Test Generator Tool for C++ (LLM-based)

This tool automates the generation and refinement of unit tests for C++ code using a large language model (LLM). It follows an iterative workflow:

1. Analyze C++ source code.
2. Generate initial unit tests using an LLM.
3. Build and run the tests, collecting feedback (build errors, test failures, coverage).
4. Refine tests based on feedback.
5. Repeat until tests pass and coverage is satisfactory.

## Files
- `src/analysis.cpp`: Source code analysis utilities.
- `src/generator.py`: Python script to orchestrate the workflow and interact with the LLM.
- `test/`: Directory for generated unit tests.

## Usage
1. Place your C++ source files in `src/`.
2. Run `python src/generator.py` to generate and refine tests.
3. Review results in `test/` and build/run using CMake.

---

## Requirements
- Python 3.x
- Access to an LLM API (e.g., OpenAI GPT)
- CMake, a C++ compiler, and Google Test (or similar framework)

---

## Example Workflow
1. The tool reads `src/main.cpp`.
2. It generates `test/test_main.cpp` with initial tests.
3. It builds and runs the tests, collecting feedback.
4. It refines the tests based on build/test results.
5. The process repeats until tests pass and coverage is improved.

---

## Extending
- Add more analysis logic in `src/analysis.cpp`.
- Customize LLM prompts in `src/generator.py`.
