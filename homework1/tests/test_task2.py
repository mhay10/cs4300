from src import task2
import pytest

# Make sure all datatypes match
@pytest.mark.parametrize(
    "key, expected_type",
    [
        ("int", int),
        ("float", float),
        ("str", str),
        ("bool", bool),
    ],
)
def test_datatypes(key, expected_type):
    datatypes = task2.get_datatypes()
    assert type(datatypes[key]) == expected_type

# Run tests
if __name__ == "__main__":
    test_datatypes()
