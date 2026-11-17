from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

# Generate an RSA private and public key pair

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    )

public_key = private_key.public_key()

# Get a message from the user to sign
message = input("Enter a message to sign: ").encode()

# Sign the message using the private key
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("\nOriginal message: ", message.decode())
print("Signature: ", signature.hex())

# Verify the signature using the public key
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature is valid.")
except InvalidSignature:
    print("Signature is invalid.")

# test verification with a modified message
modified_message = message + b" modified"

try:
    public_key.verify(
        signature,
        modified_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Modified message signature is valid.")
except InvalidSignature:
    print("Modified message signature is invalid.")