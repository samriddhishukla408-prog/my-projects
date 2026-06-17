char = input("Enter a single alphabet: ").lower()
if len(char) != 1 or not char.isalpha():
    print("Invalid input. Please enter a single alphabet.")
elif char in ['a', 'e', 'i', 'o', 'u']:
    print(char.upper(), "is a Vowel")
else:
    print(char.upper(), "is a Consonant")