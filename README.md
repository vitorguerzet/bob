# MATPOWER Case Project

This project creates a MATPOWER case and tests it.

## Structure

- `matpower_classes/`: Contains the main code for creating MATPOWER classes and case generation methods.
- `tests/`: Contains unit tests for the project.
- `requirements.txt`: List of dependencies.
- `run_case.py`: Script to run the case creation.

## How to Run

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the case creation:

    ```bash
    python create_case.py
    ```

3. Run tests:

    ```bash
    python -m unittest discover tests
    ```
