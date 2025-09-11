from src import task6
import tempfile
import pytest

# Test count_words counts words in provided file correctly
def test_provided_file():
    assert task6.count_words("task6_read_me.txt") == 106

# Test count_words raises error if file does not exist
def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        task6.count_words("invalid_file.txt")

# Test count_words with custom files
@pytest.mark.parametrize(
    "text, result",
    [
        ("Hello World!", 2),
        ("I'm sorry Dave. I'm afraid I can't do that.", 9),
        ("", 0),
    ]
)
def test_custom_files(text, result):
    # Create temp file
    with tempfile.NamedTemporaryFile(mode="w") as f:
        f.write(text)
        f.seek(0)
        assert task6.count_words(f.name) == result


# Run tests
if __name__ == "__main__":
    pytest.main([__file__, "-v"])