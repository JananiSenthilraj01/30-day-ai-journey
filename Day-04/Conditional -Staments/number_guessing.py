secret = 25

guess = int(input("Guess the number: "))

if guess == secret:
    print("Correct!")
elif guess > secret:
    print("Too High")
else:
    print("Too Low")
