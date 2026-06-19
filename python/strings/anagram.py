word1 = input("Enter first word: ").lower().replace(" ", "")
word2 = input("Enter second word: ").lower().replace(" ", "")
 
if sorted(word1) == sorted(word2):
    print(word1, "and", word2, "are Anagrams")
else:
    print(word1, "and", word2, "are NOT Anagrams")