def binary_to_decimal(binary_str):
    try:
        decimal = int(binary_str, 2)
        return decimal
    except ValueError:
        return "Invalid binary number!"
def octal_to_hexadecimal(octal_str):
    try:
        decimal = int(octal_str, 8)
        hexa = hex(decimal).upper().replace("0X","")
        return hexa
    except ValueError:
        return "Invalid octal number!"
print("Number System Conversion")
print("1. Binary to Decimal")
print("2. Octal to Hexadecimal")
choice = input("Enter your choice (1 or 2): ")
if choice == "1":
    binary_str = input("Enter the binary number: ")
    print("Decimal value:", binary_to_decimal(binary_str))
elif choice == "2":
    octal_str = input("Enter the octal number: ")
    print("Hexadecimal value:", octal_to_hexadecimal(octal_str))
else:
    print("Invalid choice! Please enter 1 or 2.")
