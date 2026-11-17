This repository is to hold projects created for SDEV 245. 

The first project is a Role-Based Access Control example to show the hard-coded admin and user permissions check.

CIA stands for Confidentiality, Integrity, and Availability. Confidentiality protects information from unauthorized access. Integrity protects information from unautorized changes. Availability ensures authorized users can access information and systems when needed.

Because Bob has the role of a regular user, preventing him from accessing administrative functions helps maintain
confidentiality by restricting access to information and resources above his authorization level.

The second project is a symmetric and asymmetric encryption demonstration using Python. The program uses AES-GCM for symmetric encryption and RSA for asymmetric encryption. Both methods encrypt and decrypt the same plaintext message to demonstrate how each
algorithm works.
AES-GCM uses a single secret key for both the encryption and decryption processes. RSA uses a public key to encrypt the message and a private key to decrypt it. It also verifies the decrypted message matches the original message. For educational purposes,
the program can display the encryption keys when SHOW_KEYS is set to True.
AES is faster and can handle large amounts of data, whereas RSA is slower, and meant to handle smaller amounts of data. The RSA encryption solves the problem of needing to share a single secret key.
