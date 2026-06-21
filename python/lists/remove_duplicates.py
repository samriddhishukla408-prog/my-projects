numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1]
print("Original list:", numbers)

#using set as set cant have duplicates
new_list=list(set(numbers))
print(f"the new list after rremoving duplicates is: {new_list}")