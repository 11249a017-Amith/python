check=input("enter the word:\n")
if (check==check[::-1]):
    print("it is palindrome")
else:
        print("it is not palindrome")


number=input("enter the number to count the appearance:")
digit=input("enter which value to check:")
count=0
for element in number:
    if element==digit:
        count+=1
