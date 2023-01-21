import hashlib

def check_password():
    """Check if a plaintext password matches a hashed password."""
    hashed_password = input("Enter the hashed password: ")
    password = input("Enter the plaintext password: ")

    # Hash the input password
    password_hash = hashlib.sha1(password.encode()).hexdigest()

    # Compare the input hash to the stored hash
    if password_hash == hashed_password:
        print("Password is valid")
    else:
        print("Password is invalid")

check_password()
