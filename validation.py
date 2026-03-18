email_input = input("Please enter your email address: ")
phone_number_input = input("Please enter a valid phone number: ")
password_input = input("Please enter a strong password: ")


def validate_email(email):
    if not email:
        print("No email address entered")

    if "@" not in email or ".com" not in email:
        print("Invalid email address")

    return True


def validate_phone(phone):
    if not phone:
        print("No input provided")

    if len(phone) != 10:
        print("Phone number must be exactly 10 digits")

    if not phone.isdigit():
        print("Phone number must contain only digits")

    if not phone.startswith("07"):
        print("Kenyan phone numbers must start with 07")

    return True


def validate_password(password):
    if not password:
        print("No input provided")

    if len(password) < 8:
        print("Password must be at least 8 characters")

    # Check if at least one digit exists
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one number")

    return True


validate_email(email_input)
validate_phone(phone_number_input)
validate_password(password_input)
