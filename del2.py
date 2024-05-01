import random

def play_game():
    print("Let's 'Guess the Number'! I try to pick up a number between 0 and 100.")
    secret_number = random.randint(0, 100)
    guess_start = 0
    guesses_finish = 5

    while guess_start < guesses_finish:
        guess = int(input(f"You have {guesses_finish - guess_start} guesses finish. Enter your guess: "))
        guess_start += 1

        if guess < secret_number:
            print("noh! That's low. Keep trying!")
        elif guess > secret_number:
            print("wow, high. Let's see if you can get it right!")
        else:
            print(f"Well guessed, smarty pants! You found the number in {guess_start} tries!")
            break

    if guess_start >= guesses_finish:
        print(f"Auch, you didn't find the number. The number was {secret_number}.")

if __name__ == "__main__":
    play_game()