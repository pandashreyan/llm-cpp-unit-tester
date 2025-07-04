# LLM-powered C++ Unit Test Generator

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
1. **Code Analyzer**: Parses C++ source code to extract functions, classes, and dependencies.
2. **LLM Interface**: Communicates with the LLM to generate test cases.
3. **Test Generator**: Formulates prompts for the LLM based on code analysis.
4. **Build System Integrator**: Manages compilation of generated tests.
5. **Test Runner**: Executes the generated unit tests.
6. **Feedback Loop**: Analyzes test results for iterative improvement.
7. **Coverage Analyzer**: Measures test coverage.

## Files
- `src/analysis.cpp`: Source code analysis utilities
- `src/generator.py`: Python script to orchestrate workflow
- `src/functions.cpp`: Example implementation (81.82% coverage)
- `test/test_main.cpp`: Generated tests (100% coverage)
- `test/generation_instructions.yaml`: Prompt for generating tests
- `test/refinement_instructions.yaml`: Prompt for refining tests

## Usage
1. Place your C++ source files in `src/`.
2. Run `python src/generator.py` to generate and refine tests.
3. Review results in `test/` and build/run using CMake.

## Requirements
- Python 3.x
- Access to an LLM API (e.g., OpenAI GPT)
- CMake, C++ compiler, and Google Test

## Current Status
- All tests pass (168/168)
- Coverage:
  - `src/functions.cpp`: 81.82%
  - `test/test_main.cpp`: 100%

## Extending
- Add more analysis logic in `src/analysis.cpp`.
- Customize LLM prompts in `src/generator.py`.