import os


def count_words(filename: str):
    """Counts the number of words in a file"""

    # Check if the file exists
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File {filename} does not exist")

    # Open the file and count number of words in each line  
    with open(filename, "r") as f:
        lines = map(str.strip, f.readlines())
        words = sum(len(line.split()) for line in lines)
        return words


if __name__ == "__main__":
    word_count = count_words("task6_read_me.txt")
    print("Number of words:", word_count)
