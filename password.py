import random
import string

def generate_secure_password(length=24):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    password = "".join(random.choice(characters) for _ in range(length))
    return password

# Generate and print a secure password
print("Secure Password:", generate_secure_password(24))