numbers = [5, 8, 5, 2, 8, 9, 1, 2]

unique_list=list(set(numbers))
print(f"Unique List: {unique_list}")

sorted_list = sorted(unique_list)
print(f"Sorted List: {sorted_list}")

tuple=tuple(unique_list)
print(f"Tuple: {tuple}")

dict={}
for num in sorted_list:
    dict[num] = num ** 2
print(f"dictionary: {dict}")

even=set([n for n in sorted_list if n%2==0])
print(f"Even Set: {even}")