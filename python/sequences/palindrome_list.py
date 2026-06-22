list=[]
n=int(input("enter value of n"))
i=0
while i<n:
    a=int(input(f"enter {i} element "))
    list.append(a)
    i+=1

list2=[]
for i in list:
    list2.append(i)
if list==list2:
    print("plaindrome list")
else:
    print("not palindrome")

#using reverse slicing
num=[1, "abc",78, 34, "abc", 1]
if num[0:]== num[::-1]:
    print("plaindrome list")
else:
    print("not palindrome")

