# Python Program to Read a String from the User and Append it into a File

file = "file.txt"


def append_string_to_file(file: str, s: str) -> None:
    with open(file, "a") as f:
        f.write(s)
        f.write("\n")


s = input("Enter a string: ")
append_string_to_file(file, s)
