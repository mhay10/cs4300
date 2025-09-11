from contextlib import redirect_stdout
from io import StringIO
from src import task1
import sys


def test_output():
    output = StringIO()
    with redirect_stdout(output):
        task1.greet()
        assert output.getvalue().strip() == "Hello, World!"


if __name__ == "__main__":
    test_output()