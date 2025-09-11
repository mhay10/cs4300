from src import task6
import pytest

# Test count_words counts words in provided file correctly
def test_provided_file():
    assert task6.count_words("task6_read_me.txt") == 106

# Test count_words raises error if file does not exist
def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        task6.count_words("invalid_file.txt")

# Run tests
if __name__ == "__main__":
    pytest.main([__file__, "-v"])