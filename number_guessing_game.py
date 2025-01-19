import random
import time
start_time = 0
end_time = 0
def welcome():
    print("Welcome to the Number Guessing Game!")
    while True:
        try:
            difficulty = int(input("To start, please choose a difficulty: (1: Easy), (2: Medium), (3: Hard): "))
            if difficulty == 1 or difficulty == 2 or difficulty == 3:
                play_game(difficulty)
                return
            else:
                print("Number must be from 1 to 3")
        except:
            print("Please enter a valid number")
def random_number():
    return(random.randint(1, 100))
def get_hint(actual_number):
    while True:
        try:
            l, r = map(int, input(f"Enter {"l r"} to specify your range: ").split())
            if l <= actual_number <= r:
                print("Your number is in the range!")
            else:
                print("Your number is not in the range")
            return
        except:
            print("Enter a valid pair of intergers")
def play_game(difficulty):
    global start_time
    start_time= time.time()
    print("I'm thinking of a number from 1 to 100. You could type 0 to use a hint. A hint allows you to specify a range and the computer will tell you if the number is in that range or not. You have one hint per round")
    actual_number = random_number()
    chances = 0
    hint = 1
    if difficulty == 1:
        chances = 20
    elif difficulty == 2:
        chances = 10
    else:
        chances = 6
    print(f"You have {chances} chances to guess")
    while chances > 0:

        while True:
            try:
                user_guess = int(input("Enter your guess: "))
                if user_guess >= 1 and user_guess <= 100:
                    process_guess(user_guess, actual_number)
                    chances = chances - 1
                    print(f"You have {chances} chance(s) left")
                    break
                elif user_guess == 0:
                    if hint == 0:
                        print("You are out of hint")
                    else:
                        get_hint(actual_number)
                        hint = hint - 1
                else:
                    print("Number must be between 0 and 100")
            except:
                print("Enter a valid number between 0 and 100")
    user_lose()


def process_guess(guess, value):
    if guess == value:
        user_won()
    elif guess < value:
        print("Your number was too small")
    else:
        print("Your number was too big")
def user_won():
    print("Congratulations! You won!")
    global end_time
    end_time = time.time()
    print(f"It took you {round(end_time - start_time, 0)} seconds")
    play_again()
    pass
def user_lose():
    print("Game Over. Better luck next time")
    play_again()
def play_again():
    while True:
        prompt = input("Do you want to play again? (Y/N)")
        if prompt == 'Y':
            print("Ok!")
            welcome()
            return
        elif prompt == 'N':
            print("See you soon!")
            return
        else:
            print("Enter a valid option")

if __name__ == "__main__":
    welcome()

