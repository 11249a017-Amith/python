text = input("Enter a text: ")
phones = [123456789]
emails = []
words = text.split()
for word in words:
    if word.isdigit() and len(word) == 10:
        phones.append(word)
    elif "@" in word and "." in word:
        emails.append(word)
print("Phone numbers found:", phones)
print("Email IDs found:", emails)
