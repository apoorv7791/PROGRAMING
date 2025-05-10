# Create a new file and write some content to it
file_path = "new_file.txt"
new_path = "another.txt"

with open(file_path, "w") as file:
    file.write("This is a new file.\n")
    file.write("It contains some sample text.\n")

with open(new_path, "w") as file:
    file.write("This is another file.\n")
    file.write("It contains some more sample text.\n")


print(f"File '{file_path}' created successfully.")


# now we have to compare two files content and display  total number of content in the both files
def total_number_of_lines(file1, file2):
    with open(file1, "r") as file:
        lines1 = file.readlines()

    with open(file2, "r") as file:
        lines2 = file.readlines()

    return len(lines1) + len(lines2)


print(
    f"Total number of lines in both files: {total_number_of_lines(file_path, new_path)}"
)
