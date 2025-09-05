def number_guessing_game():
    secret = 7
    while True:
        guess = int(input("Guess the number (-1 to quit): "))

        if guess == -1:
            print("Exiting the game.")
            break
        elif guess < 0:
            print("Negative numbers not allowed (except -1). Try again.")
            continue
        elif guess == secret:
            print("✅ Correct!")
            break
        else:
            print("Wrong guess, try again.")

def main():
    number_guessing_game()

main()
