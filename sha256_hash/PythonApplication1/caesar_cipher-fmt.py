
# Encrypt a message using a caesar cipher given a shift value

def encrypt(message, shift):
    result = ""

    for char in message:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result