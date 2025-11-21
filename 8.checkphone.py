number = input("Enter phone number: ")
if number.isdigit() and len(number) == 10:
    print("Valid phone number")
else:
    print("Invalid phone number")
