from contextlib import redirect_stdout
from io import StringIO
from src import task1
import pytest
import sys

# Make sure output matches
def test_output():
    # Redirect output into temp buffer to check output
    output = StringIO()
    with redirect_stdout(output):
        task1.greet()
        assert output.getvalue().strip() == "Hello, World!"

# Run test
if __name__ == "__main__":
    pytest.main([__file__, "-v"])