string = input("Enter a word or phrase: ").lower()
# Clean the string — remove spaces
new = string.replace(" ", "")
if new == new[::-1]:
    print(string, "is a Palindrome")
else:
    print(string, "is NOT a Palindrome")