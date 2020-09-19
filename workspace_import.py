import random
    
random_number = ()
guessed_number = ()
score_count = []
    
 
print("Hello, welcome to the Number-Guessing Game!\n")
print("The objective of this game is to correctly identify an unknown, randomly generated number in as few guesses as possible. The number is between 1 - 10.")
print("The number is between 1 - 10.\n")

while True:
    
    user_input = input("Would you like to play (another) round? (Y/N)  ")
    game_proceed = user_input.lower()
    
    if game_proceed == "n":
        print("\nOkay, well, suit yourself!")
        break
    
    elif game_proceed == "y":
        print(f"Your best score so far is {min(score_count)}. Try to beat it this time!\n")
        random_number = random.randint(1, 10)
        guess_count = 0
        
        while True:
            try:
                guessed_number = int(input("Enter a number: "))
        
            except ValueError:
                print("Oops!  That was not valid value.  Try again...\n")
                continue
                
            if guessed_number > 10:
                print("Sorry, that's not a valid number - it's too high!\n Remember, choose a number 1 through 10.\n\n")
                continue
                
            elif guessed_number < 1:
                print("Sorry, that's not a valid number - it's too low!\n Remember, choose a number 1 through 10.\n")
                continue
                
            elif (guessed_number > random_number):
                print(f"{guessed_number} is too high!\n")
                guess_count += 1
                continue
            
            elif (random_number > guessed_number):
                print(f"{guessed_number} is too low!\n")
                guess_count += 1
                continue
            
            elif (guessed_number == random_number):
                guess_count += 1
                score_count.append(guessed_number)
                print(f"{guessed_number} is correct!")
                break
        
        print(f"Nice job! That took you {guess_count} guesses!\n\n")
        continue
        
    elif game_proceed == 'exit':
        break
    
    else:
        print("Please input 'Y' or 'N'. \n")
        
        
print(f"You played {len(score_count)} rounds, and the lowest number of guesses it took you to guess correctly was {min(score_count)}. Not bad! \n")
print("Have a nice day, and hope to see you around here again!")
