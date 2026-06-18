num = int(input("Enter a number: "))
reverse = 0
original=num
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if reverse== original:
    print("palindrome number")
else:
    print("not a palindrome number")
