from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

# Generate an RSA private and public key pair

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    )

public_key = private_key.public_key()