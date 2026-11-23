#نیما مرتضائی
def decrypt(cipher_text, key):
    decrypted_text = ""

    for char in cipher_text:

        if char.isupper():
            decrypted_char = chr(
                (ord(char) - ord('A') - key) % 26 + ord('A')
            )
            decrypted_text += decrypted_char

        elif char.islower():
            decrypted_char = chr(
                (ord(char) - ord('a') - key) % 26 + ord('a')
            )
            decrypted_text += decrypted_char

        else:
            decrypted_text += char

    return decrypted_text


# Get input from user
cipher_text = input("Enter your cipher text: ")
key = int(input("Enter decryption key: "))

# Decrypt the text
result = decrypt(cipher_text, key)

print("Decrypted text:", result)
