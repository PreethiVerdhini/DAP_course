#program 5 : Check if a password contains at least 1 uppercase letter, 1 lowercase letter, 1 digit, and is at least 8 characters long

password = input("Enter a password: ")


upper = any(char.isupper() for char in password)
lower = any(char.islower() for char in password)
digit = any(char.isdigit() for char in password)
length = len(password) >= 8


if upper and lower and digit and length:
    print("Password is valid.")
else:
    print("Password is invalid.")
    print("It must contain at least:")
    if not upper:
        print("- One uppercase letter")
    if not lower:
        print("- One lowercase letter")
    if not digit:
        print("- One digit")
    if not length:
        print("- Minimum 8 characters")
