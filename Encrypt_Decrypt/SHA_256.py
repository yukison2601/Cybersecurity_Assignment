import hashlib

def sha256_converter(input_string):
    # Create a new SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Convert the input string to bytes and update the hash object
    sha256_hash.update(input_string.encode('utf-8'))

    # Get the hexadecimal representation of the hash value
    hashed_value = sha256_hash.hexdigest()

    return hashed_value

# Example usage
input_string = "Jgnnq!Yqtnf"
hashed_value = sha256_converter(input_string)
print("Input String:", input_string)
print("SHA-256 Hash:", hashed_value)
