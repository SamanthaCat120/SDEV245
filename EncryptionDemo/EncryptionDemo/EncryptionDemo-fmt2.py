import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Generate a random 256-bit key
secret_key = AESGCM.generate_key(bit_length=256)

# Create an AESGCM cipher
cipher = AESGCM(secret_key)

# Original plaintext message
message = "Hello World! This is a secret message."

# Generate a random 12-byte nonce (number used once)