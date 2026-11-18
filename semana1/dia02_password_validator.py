print("===== PASSWORD VALIDATION =====")
print("""
Your password must contain:
- at least 8 characters
- at least 1 uppercase letter
- at least 1 number
""")

while True:
    password = input("Create a password: ")
    has_digit = False # Flags
    has_upper = False

    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True

    is_valid = True
    if len(password) < 8:
        print("! Password must contain at least 8 characters.")
        is_valid = False
    if not has_upper:
        print("! Password must contain at least one uppercase letter.")
        is_valid = False
    if not has_digit:
        print("! Password must contain at least one number")
        is_valid = False

    if is_valid:
        print("Password is valid.")
        break

    print("Password is not valid. Try again.")