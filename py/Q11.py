# Wrtie a program that encrypts a message by adding a key vlaue to every character (Caesar Cipher) (input: “abc”. output: “def” , Add3 to each every character)
def caesar_cipher(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift = ord("a") if char.islower() else ord("A")
            encrypted_message += chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted_message += char
    return encrypted_message


# Example usage
message = "abc"
key = 3
encrypted_message = caesar_cipher(message, key)
print(f"Original message: {message}")
print(f"Encrypted message: {encrypted_message}")
