import random

def guess():
    user = input("Enter your name: ")
    while True:
        ref_guess = random.randint(1, 100)
        print(f"\nHey {user}!, Welcome to the Number Guessing Game!!!")
        print ()
        print("I'm thinking of a number between 1 and 100.")
        attempts = 0

        while True:
            try:
                user_guess = int(input('\nTake a guess: '))
                if user_guess < 1 or user_guess > 100:
                    print("Ah! The number is my mind is between 1 and 100.")
                    continue
                attempts += 1
                if user_guess < ref_guess:
                    print('Try a higher number!')
                elif user_guess > ref_guess:
                    print('Try a lower number!')
                else:
                    print(f'Congratulations! You guessed the number in {attempts} attempts.')
                    break
            except ValueError:
                print('Please enter a valid number.')

        play_again = input("Do you want to play again? (Y/N): ").strip().upper() #the strip and upper functions help eliminate any user input errors like extra space or case differences.
        if play_again != 'Y':
            print(f'Thanks for playing, {user}! Goodbye!')
            break

guess()
#print
