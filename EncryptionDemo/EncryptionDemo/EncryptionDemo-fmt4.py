import os
from wsgiref.simple_server import demo_app
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

# Display secret keys for educational demonstration
SHOW_KEYS = True

print("=" * 60)
print("SYMMETRIC AND ASYMMETRIC ENCRYPTION DEMONSTRATION")
print("=" * 60)


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

print("\n" + "-" * 60)
print("SYMMETRIC ENCRYPTION (AES-GCM)")
print("-" * 60)
print("Original Message:", message)
if SHOW_KEYS:
    print("Secret key:", secret_key.hex())
print("Encrypted Message:", encrypted_message.hex())

# Decrypt the encrypted message
decrypted_message = cipher.decrypt(nonce, encrypted_message, None)

# Convert decrypted bytes back to string
decrypted_message_str = decrypted_message.decode()

# Display the decrypted message
print("Decrypted Message:", decrypted_message_str)

# ASYMMETRIC ENCRYPTION (RSA)

# Generate RSA private key

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Generate corresponding public key

public_key = private_key.public_key()

# Convert the public key to a readable format (PEM)

public_key_text = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Convert the private key to a readable format (PEM)

private_key_text = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Display the keys

print("\nASYMMETRIC ENCRYPTION (RSA)")
print("Public Key:\n", public_key_text.decode())

if SHOW_KEYS:
    print("Private Key:\n", private_key_text.decode())

# Encrypt the message using the public key
rsa_encrypted_message = public_key.encrypt(
    message.encode(),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Original Message:", message)
print("Encrypted Message (RSA):", rsa_encrypted_message.hex())