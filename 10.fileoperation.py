filename = input("Enter the file name: ")
n = int(input("Enter how many lines to display: "))
with open(filename, "r") as file:
    lines = file.readlines()
print("\n-- First", n, "lines of the file --")
for i in range(min(n, len(lines))):
    print(lines[i], end="")
word = input("\nEnter a word to count in the file: ")
count = 0
for line in lines:
    count += line.count(word)
print("The word", word, "occurs", count, "times in the file.")
