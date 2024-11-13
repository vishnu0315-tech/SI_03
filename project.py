def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift_amount = shift % 26
            start = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            encrypted_text += char  # Non-alphabetic characters are not changed
    return encrypted_text

def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift % 26
            start = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - start - shift_amount) % 26 + start)
        else:
            decrypted_text += char  # Non-alphabetic characters are not changed
    return decrypted_text

# Example usage
if __name__ == "__main__":
    text = "Hello World! This is a Caesar Cipher."
    shift = 3  # Shift by 3 positions

    encrypted = caesar_encrypt(text, shift)
    print(f"Encrypted Text: {encrypted}")

    decrypted = caesar_decrypt(encrypted, shift)
    print(f"Decrypted Text: {decrypted}")
