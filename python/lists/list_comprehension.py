numbers = list(range(1, 11))
print("Numbers:", numbers)
squares = [n ** 2 for n in numbers]
print("Squares:", squares)
evens = [n for n in numbers if n % 2 == 0]
print("Even numbers:", evens)
odd_squares = [n ** 2 for n in numbers if n % 2 != 0]
print("Squares of odd numbers:", odd_squares)
words = ["python", "java", "c", "javascript"]
long_words = [word.upper() for word in words if len(word) > 3]
print("Words longer than 3 letters (uppercase):", long_words)
 
 