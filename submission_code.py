# Below are the list of of imported modules and defined variables used in this program.
# Random module & function found at https://docs.python.org/3.1/library/random.html.
import random
    
random_number = ()
guess_count = ()
guessed_number = ()
score_count = []
play_game = ()

# This function 'start_game' displays a short message at the start of the game to welcome the user, clarify the purpose of this program, and clarify the aims/ contraints of the game.
def start_game():
    print("\n Hello & Welcome to...")
    print(">>>>>>>>>> TheNumber-Guessing Game <<<<<<<<<<\n")
    print("* The objective of this game is to correctly identify an unknown, randomly generated number.")
    print("* And.. to do this in as few guesses as possible!")
    print("* The hidden number is between 1 - 10.")
    print("* Try playing multiple rounds to obtain the best score possible.\n")
    
# This function prompts users for input, confirming whether or not they would like to try playing the game. If the value is neither "Y" or "N", the user is prompted to return the input again until is matches one of these values.  If the value is 'y', the main 'play' part of the program is run, if not, they are directl given the end_game message.
# A main part of this function was suggest to me by Jennifer Nordell is the Slack forum.
def get_play_game():
    play_game = None
    while play_game != "y" and play_game != "n":
        play_game = input("Would you like to try playing the game? [Y/N]: ").lower()
    return play_game
    
# This function prompts users for input, confirming whether or not they would like to play another round of the game. If the value is 'y', the program cycles through another round of play. If not, the while loops ends, activating the end_game part of the program.
def get_play_again():
    
    play_again = None
    while play_again != "y" and play_again != "n":
        play_again = input("Would you like to play again? [Y/N]: ").lower()
    return play_again
    
# This function is used at the end of the program. It displays a farewell message, indicating that the game and the program are at its finish. And if the user has play any rounds, both (a) the number of rounds they have played and (b) their best (lowest) score are display to the user; as well as a personalized message that depends on the range that the best score falls within.
def end_game():
    if len(score_count) == False:
        print("\nAlright, well, thanks for stopping by anyway.")
        print("But when you come by next, how about giving the game a try, huh? \n")
      
    else:
        print("\n")
        print(f"You played: {len(score_count) + 1} Rounds")
        print(f"The lowest number of guesses it took you to guess correctly was: {min(score_count)}. ")
        if 2 >= (min(score_count)):
            print("That's super! \n")
        elif 3 >= (min(score_count)):
            print("Not bad, not bad at all! \n")
        else:
            print("That's okay I suppose. But better luck to you next time , eh? \n")
        print("Well, I guess that's all then..")
        print("Thanks for giving the game a go!")
        print("Have a nice day, and hope to see you around here again!")

# The main logic of program begins here: The game is started, the user is prompted for whether they would like to play. If they would like to play, the  program runs a while loop. The while loops runs through  one round of play, first establishing the hidden number and round number, and then prompting the user for guesses. Invalid guesses are rejected, and the number of valid guesses are counted until the number is finally correctly identified. At which point the number of guesses, and the user's best score so far is display. The user is also prompted whether they'd like to play. If so, they are looped through again for another round. If not, the loop ends and the programs runs an end game  display message that varies based on user participation and performance.
    
start_game()

play_game = get_play_game()
        
if play_game == "y":
    
    play_again = "y"
    
    while play_again == "y":
            
        print(f"\nWelcome to Round {len(score_count) + 1}!")
        
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
                score_count.append(guess_count)
                print(f"{guessed_number} is correct! \n")
                print(f"That took you {guess_count} guesses. Nice job!")
                break
        
        print(f"Your best score so far is {min(score_count)} guesses.\n")
    
        play_again = get_play_again()
        
     
end_game()