sentence = input("Enter a sentence: ")
words = sentence.split()
num_words = len(words)
num_digits = 0
num_upper = 0
num_lower = 0
for ch in sentence:
    if ch.isdigit():
        num_digits += 1
    elif ch.isupper():
        num_upper += 1
    elif ch.islower():
        num_lower += 1

print("Number of words:", num_words)
print("Number of digits:", num_digits)
print("Number of uppercase letters:", num_upper)
print("Number of lowercase letters:", num_lower)
