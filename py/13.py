def count_word_occurrences(file_path, word):
    try:
        with open(file_path, "r") as file:
            text = file.read()
            word_count = text.lower().split().count(word.lower())
            return word_count
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return 0


# Example usage
file_path = "file.txt"  # Replace with your text file path
word = "python"  # Replace with the word you want to count
count = count_word_occurrences(file_path, word)
print(f"The word '{word}' occurs {count} times in the file.")
