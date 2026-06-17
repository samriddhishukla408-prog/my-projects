month = int(input("Enter month number (1-12): "))
if month < 1 or month > 12:
    print("Invalid month number")
elif month in [1, 3, 5, 7, 8, 10, 12]:
    print("This month has 31 days")
elif month in [4, 6, 9, 11]:
    print("This month has 30 days")
else:
    print("This month(february) has 28 days ( 29 in Leap Year)")
