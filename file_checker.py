
import hashlib
import os

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


file_path = input("Enter file path: ")

if os.path.isfile(file_path):
    result = calculate_hash(file_path)
    print("SHA-256 Hash:", result)
else:
    print("File not found!")
