import hashlib

# Generate a 256-bit hash of a message using SHA-256
message = input("Enter a message to hash: ")
hash_object = hashlib.sha256(message.encode())
print("Original message: ", message)
print("SHA-256 hash: ", hash_object.hexdigest())

# Generate a SHA-256 hash of a file
def hash_file(file_path):
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()

file_path = input("\nEnter the path of the file to hash: ")

if file_path:
    try:
        file_hash = hash_file(file_path)
        print(f"\nSHA-256 hash of the file '{file_path}': {file_hash}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")