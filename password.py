import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    letters = string.ascii_letters
    digits = string.digits if use_digits else ""
    symbols = string.punctuation if use_symbols else ""

    all_chars = letters + digits + symbols

    if not all_chars:
        print("No character sets selected.")
        return ""

    password = "".join(random.choice(all_chars) for _ in range(length))
    return password


def main():
    print("=== Random Password Generator ===")
    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Invalid input. Using default length 12.")
        length = 12

    use_digits = input("Include digits? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    password = generate_password(length, use_digits, use_symbols)
    print(f"\nGenerated Password: {password}")


if __name__ == "__main__":
    main()
