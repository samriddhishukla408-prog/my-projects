num = int(input("Enter a number: "))
x = num
sum = 0
while num > 0:
    digit = num % 10
    sum += digit ** 3
    num= num // 10
if sum == x:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")