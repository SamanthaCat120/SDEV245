
# Encrypt a message using a caesar cipher given a shift value

def encrypt(message, shift):
    result = ""

    for char in message:
        if char.isascii() and char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Decrypt a message using a caesar cipher given a shift value 

def decrypt(message, shift):
    return encrypt(message, -shift)

message = input("Enter a message: ")
shift = int(input("Enter a shift value (1-25): "))

encrypted_message = encrypt(message, shift)
decrypted_message = decrypt(encrypted_message, shift)

print("\nOriginal message: ", message)
print("Encrypted message: ", encrypted_message)
print("Decrypted message: ", decrypted_message)