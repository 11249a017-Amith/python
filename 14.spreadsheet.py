.class Check:
    def check_palindrome(self, data):
        s = str(data)
        return s == s[::-1]
obj = Check()
print(obj.check_palindrome("wow"))
print(obj.check_palindrome("18"))

15.import openpyxl

# Load existing Excel file
read_wb = openpyxl.load_workbook("input.xlsx")
read_sheet = read_wb.active
print("Reading data from input.xlsx:")
for row in read_sheet.iter_rows(values_only=True):
    print(row)
# Create a new Excel file
write_wb = openpyxl.Workbook()
write_sheet = write_wb.active
# Write header
write_sheet.append(["Name", "Marks"])
# Sample data to write
data = [
    ["jithu", 88],
    ["dosth", 92],
    ["lucky", 79]
]

# Write data rows
for row in data:
    write_sheet.append(row)

# Save new file
write_wb.save("output.xlsx")

print("\nData written to output.xlsx successfully!")
