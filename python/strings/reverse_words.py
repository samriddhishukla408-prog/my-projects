sentence = input("Enter a sentence: ")
words = sentence.split()
# Reverse each word
reversed_words = [word[::-1] for word in words]
result = " ".join(reversed_words)
print("Each word reversed:", result)
 
