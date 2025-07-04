# LLM-powered C++ Unit Test Generator

## Project Goal
To develop a tool that automatically generates and refines unit tests for C++ applications using a Large Language Model (LLM).

## Architecture Overview

### Components:
1.  **Code Analyzer**: Parses C++ source code to extract functions, classes, and dependencies.
2.  **LLM Interface**: Communicates with the LLM to generate test cases.
3.  **Test Generator**: Formulates prompts for the LLM based on code analysis and integrates generated tests into a test framework (e.g., Google Test).
4.  **Build System Integrator**: Manages the compilation of generated tests and the application code.
5.  **Test Runner**: Executes the generated unit tests and captures results.
6.  **Feedback Loop / Refinement Engine**: Analyzes test results (failures, coverage) and provides feedback to the LLM for iterative improvement.
7.  **Coverage Analyzer**: Measures test coverage to identify areas needing more tests.

## Workflow:

### 1. Generate Unit Tests:
-   **Input**: C++ source code files.
-   **Process**: The Code Analyzer extracts relevant code snippets (functions, classes). The Test Generator crafts prompts for the LLM, requesting unit tests for specific code units. The LLM Interface sends these prompts and receives generated test code. The generated tests are then integrated into a test file.

### 2. Refine Tests Based on Feedback:
-   **Input**: Initial test results (pass/fail) and potentially build errors.
-   **Process**: If tests fail or build errors occur, the Feedback Loop analyzes the issues. It then generates new prompts for the LLM, explaining the failures/errors and requesting corrections or improvements to the test cases. This process iterates until tests pass and build issues are resolved.

### 3. Handle Build Issues and Improve Test Coverage:
-   **Input**: Build logs, test results, coverage reports.
-   **Process**: The Build System Integrator attempts to compile the tests. If compilation fails, the Feedback Loop uses the build errors to inform the LLM for corrections. After successful compilation, the Test Runner executes tests. The Coverage Analyzer identifies code paths not covered by existing tests. The Feedback Loop then prompts the LLM to generate additional tests to increase coverage.

## Next Steps:
1.  Set up a basic C++ project structure.
2.  Integrate a testing framework (e.g., Google Test).
3.  Implement the Code Analyzer to parse C++ files.
4.  Develop the LLM Interface to communicate with a chosen LLM.

## Assignment Requirements & Completion Checklist
- Environment setup: Complete (CMake, Google Test, Windows/WSL instructions)
- Test generation: Automated via LLM, YAML instructions present
- Test refinement: Applied (see YAML files)
- Build & debug: All tests pass (168/168), coverage measured
- Coverage results: functions.cpp – 81.82%, test_main.cpp – 100%

## YAML Instruction Files
- `test/generation_instructions.yaml`: Prompt for generating tests
- `test/refinement_instructions.yaml`: Prompt for refining tests

## Test Coverage Results
- `src/functions.cpp`: 81.82%
- `test/test_main.cpp`: 100%

## Approach Summary
- LLM analyzes code, generates and refines tests using YAML prompts, builds/tests project, and measures coverage