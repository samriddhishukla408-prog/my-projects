sentence = "the quick brown fox jumps over the lazy dog the fox runs"
words = sentence.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print("Word frequency:")
for word, count in frequency.items():
    print(f"{word}: {count}")

most_common = max(frequency, key=frequency.get)
print("Most frequent word:", most_common, "with count", frequency[most_common])