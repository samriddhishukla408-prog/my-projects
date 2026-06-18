secret = 7
guess = 0
while guess != secret:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret:
        print("Correct!")
    else:
        print("Try Again!")