text = input("Enter a sentence: ").lower()
vowels = "aeiou"
count = 0
for char in text:
    if char in vowels:
        count += 1 
print("Number of vowels:", count)

#for each vowel;
# vowel_counts = {v: 0 for v in vowels}
# for char in text:
#     if char in vowels:
#         vowel_counts[v] += 1
 
# print("Vowel breakdown:", vowel_counts)