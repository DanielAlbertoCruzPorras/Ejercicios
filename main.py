# Exercise 14: Letter Guessing Game
secret_letter = 'A'

guess = input("Guess the secret letter (one letter): ").upper()

match guess:
    case "A":
        print("You guessed it! The secret letter is A.")
    case _:
        print("Wrong guess! Try again.")


