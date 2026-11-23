#نیما مرتضائی
def encrypt(plain_text, key):
    encrypted_text = ""

    for char in plain_text:

        if char.isupper():
            encrypted_char = chr(
                (ord(char) - ord('A') + key) % 26 + ord('A')
            )
            encrypted_text += encrypted_char

        elif char.islower():
            encrypted_char = chr(
                (ord(char) - ord('a') + key) % 26 + ord('a')
            )
            encrypted_text += encrypted_char

        else:
            encrypted_text += char

    return encrypted_text


# Get input from user
plain_text = input("Enter your plain text: ")
key = int(input("Enter encryption key: "))

# Encrypt the text
result = encrypt(plain_text, key)

print("Encrypted text:", result)
