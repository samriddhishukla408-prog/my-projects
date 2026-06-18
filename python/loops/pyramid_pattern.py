rows = int(input("Enter number of rows: "))
i = 1
while i <= rows:
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)
    i += 1