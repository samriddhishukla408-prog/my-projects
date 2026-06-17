a= int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Before swap: a =", a, ", b =", b)
#using third variable
temp = a
a = b
b = temp
print("After swap (using temp): a =", a, ", b =", b)
# without temp:
a,b=b,a
print("After swap (without temp): a =", a, ", b =", b)
