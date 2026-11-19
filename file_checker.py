

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
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    file_hash = calculate_hash(file_path)

    print("\n--- FILE DETAILS ---")
    print("File Name:", file_name)
    print("File Size:", file_size, "bytes")
    print("SHA-256 Hash:", file_hash)

else:
    print("File not found!")
