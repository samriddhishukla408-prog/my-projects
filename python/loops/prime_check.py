num = int(input("Enter a number: "))

if num < 2:
    print("Not Prime")
else:
    i = 2
    prime = True

    while i < num:
        if num % i == 0:
            prime = False
            break
        i += 1

    if prime:
        print("Prime Number")
    else:
        print("Not Prime")