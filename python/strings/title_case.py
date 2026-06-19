sentence = input("Enter a sentence: ")
words = sentence.split() 
title_list = []
for word in words:
    x = word[0].upper() + word[1:].lower()
    title_list.append(x)
 
result = " ".join(title_list)
print("Title Case:", result)