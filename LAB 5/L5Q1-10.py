def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

text_to_encrypt = input("Enter the text to encrypt: ")
shift_value = int(input("Enter the shift value: "))

encrypted_text = caesar_encrypt(text_to_encrypt, shift_value)
print(f"Encrypted text: {encrypted_text}")
