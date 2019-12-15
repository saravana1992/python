secret = 1
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("enter your guess : "))
    guess_count += 1
    if guess == secret:
        print("you won")
        break
else:
    print("you are done mm, get lost :-(")