email_input = input("Please enter your email address: ")
phone_number_input = input("Please enter a valid phone number: ")
password_input = input("Please enter a strong password: ")


def validate_email(email):
    is_valid = True

    if not email:
        print("No email address entered")
        is_valid = False
    elif "@" not in email or ".com" not in email:
        print("Invalid email address")
        is_valid = False

    return is_valid


def validate_phone(phone):
    is_valid = True

    if not phone:
        print("No input provided")
        is_valid = False
    elif len(phone) != 10:
        print("Phone number must be exactly 10 digits")
        is_valid = False
    elif not phone.isdigit():
        print("Phone number must contain only digits")
        is_valid = False
    elif not phone.startswith("07"):
        print("Kenyan phone numbers must start with 07")
        is_valid = False

    return is_valid


def validate_password(password):
    is_valid = True

    if not password:
        print("No input provided")
        is_valid = False
    elif len(password) < 8:
        print("Password must be at least 8 characters")
        is_valid = False
    elif not any(char.isdigit() for char in password):
        print("Password must contain at least one number")
        is_valid = False

    return is_valid


print(f"Email: {'Valid' if validate_email(email_input) else 'Invalid'}")
print(f"Phone: {'Valid' if validate_phone(phone_number_input) else 'Invalid'}")
print(f"Password: {'Valid' if validate_password(password_input) else 'Invalid'}")