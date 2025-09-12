# CS4300 - Homework 1

This folder contains Homework 1 for CS4300.
Each task is a separate Python file in the `src` folder and has a corresponding test file in the `tests` folder.

## Installation

1. Navigate to the `homework1` folder

    ```bash
    cd cs4300/homework1
    ```

2. Create a virtual environment and activate it

    ```bash
    python -m venv venv --system-site-packages
    source venv/bin/activate
    ```

3. Install the project dependencies

    ```bash
    python3 -m pip install pytest numpy
    ```

## Running the tests

From the `homework1` folder, run the following command to run each test file:

```bash
PYTHONPATH=. python3 tests/test_task[number].py
```