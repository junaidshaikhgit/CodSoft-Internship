import random
import string

def generate_password(length):
    if length < 4:
        print("⚠ Password length should be at least 4 characters.")
        return

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_chars = lowercase + uppercase + digits + symbols

    # Generate a random password
    password = ''.join(random.choice(all_chars) for _ in range(length))

    print(f"\n🔐 Generated Password: {password}")

def main():
    print("🔑 Welcome to the Python Password Generator")
    try:
        length = int(input("Enter desired password length: "))
        generate_password(length)
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    main()
