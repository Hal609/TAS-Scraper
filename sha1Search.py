import hashlib
import os
import sys

def compute_hash(filepath):
    hash = hashlib.sha1(open(filepath,'rb').read()).hexdigest()
    # if "Mario" in filepath:
    #     print(filepath, hash)
    return hash

def find_file_by_hash(root_dir, target_hash):
    for subdir, _, files in os.walk(root_dir):
        for filename in files:
            filepath = os.path.join(subdir, filename)
            file_hash = compute_hash(filepath)
            if file_hash.lower() == target_hash.lower():
                print(f"Match found: {filepath}")
                return
    print("Not found")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <directory> <target_sha256_hash>")
        sys.exit(1)

    directory = sys.argv[1]
    target_sha1 = "A03E7E526E79DF222E048AE22214BCA2BC49C449"

    find_file_by_hash(directory, target_sha1)