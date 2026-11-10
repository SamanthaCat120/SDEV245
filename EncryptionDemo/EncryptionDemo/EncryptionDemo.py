import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Generate a random 256-bit key
secret_key = AESGCM.generate_key(bit_length=256)

# Create an AESGCM cipher
cipher = AESGCM(secret_key)

# Original plaintext message
message = "Hello World! This is a secret message."

# Generate a random 12-byte nonce (number used once)
nonce = os.urandom(12)

# Encrypt the message
encrypted_message = cipher.encrypt(nonce, message.encode(), None)

print("SYMMETRIC ENCRYTION (AES-GCM)")
print("Original Message:", message)
print("Secret key:", secret_key.hex())
print("Encrypted Message:", encrypted_message.hex())

# Decrypt the encrypted message
decrypted_message = cipher.decrypt(nonce, encrypted_message, None)

# Convert decrypted bytes back to string
decrypted_message_str = decrypted_message.decode()

# Display the decrypted message
print("Decrypted Message:", decrypted_message_str)
