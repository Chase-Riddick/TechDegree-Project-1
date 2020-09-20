# Below are the list of of imported modules and defined variables used in this program. The purpose of each is noted below.

# import random: Imports module that allows the generation of a random number.
# random_number: This empty variable will store the randomly generated number with the play_round function of the program.
# guessed_number: The user's inputted number guessed is stored in this variable, so that it can be compared against the random number.
# score_count: This is a list that stores the number of guesses it has taken the user in each round to correctly identify the random number.
# playgame_input: This empty variable stores a value that is then checked to see whether or not the user desires to (continue) play or not
# play_game:  This has the basic function of the previous variable acccept that it's modified to be in lowercase.
# round_number: This empty variable stores a value that corresponds the number of rounds played by the user. It calculated by adding +1 to the socre_count.

import random
    
random_number = ()
guessed_number = ()
score_count = []
playgame_input = ()
play_game  = ()
play_game1 = ()
play_game2 = 1
round_number = len(score_count) + 1
    
# The 'start_game' function is intended to do the following work: (a) displays a short message at the start of the game to welcome the user, clarify the purpose of this program, and clarify the aims/ contraints of the game; (b) prompts users for input, confirming whether or not they would like to try playing the game. If the value is neither "Y" or "N", the user is prompted to return the input again until is matches one of these values.
def start_game():
    
    print("Hello there! Welcome to the...\n")
    print(">>>>>>>>>> Number-Guessing Game <<<<<<<<<<\n")
    print("* The objective of this game is to correctly identify an unknown, randomly generated number. \n")
    print("* And, to do this in as few guesses as possible. \n")
    print("* The number is between 1 - 10.\n ")
    print("* If you like, play multiple rounds and try to obtain the best score possible.\n")
    
    while True:
        playgame_input = input("Would you like to play? (Y/ N) >  ")
        play_game = playgame_input.lower()
          
        if play_game == "n":
            print("\n Okay, well, suit yourself!")
            break
          
        elif play_game == "y":
            print("\n Great - Glad to hear it! Let's get started then.")
            global play_game1
            play_game1 == "y"
            break
          
        else:
            print("Please input 'Y' or 'N'. \n")
            continue

# The function 'play_round()' is intended to do most the work of this program. It contains the 'game', and repeated cycyles through rounds of play. More spefically is intended to:
# (a) generate a random number at the start of each round;
# (b) display the round number at the start of each  round;
# (c) To continue to prompt the user for a guesses (1-10) until they finally guess the randomly generated number.
# (d) To re-prompt the user for a valid guess if their former guess was outside the 1 - 10 range, or a different kind of value to prompt them again.
# (e) To count/keep track of the number of guesses the player makes to identify the number.
# (f) To display to the user their best (lowest) score.
# (g) To ask the user if they would would like to play another round. And to do some by only accept 'Y/N' response - reprompting the user for another input until one of those are give.

def play_round():
    while (play_game2) == 1:
        
        random_number = random.randint(1, 10)
        guess_count = 0
        
        print(f"Welcome to Round {round_number}!")
        
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
                print(f"{guessed_number} is correct! \n")
                print(f"That took you {guess_count} guesses. Nice job! \n\n")
                
                while True:
                    playagain_raw = input("Would you like to play (another) round? (Y/N)  ")
                    play_again =  playagain_raw.lower()
    
                    if play_again == "n":
                        print("\nOkay, well, suit yourself! \n")
                        global play_game2
                        play_game2 = 0
                        break
    
                    elif play_again == "y":
                        print(f"Your best score so far is {min(score_count)}. Try to beat it this time!\n")
                        break
                        
                    else:
                        print("Please input 'Y' or 'N'. \n")
                        continue
      
            else:
                print("Please input 'Y' or 'N'. \n")
                continue
       
# This function is used at the end of the program. It displays a farewell message, indicating that the game and the program are at its finish. And if the user has play any rounds, both (a) the number of rounds they have played and (b) their best (lowest) score are display to the user.
def end_game():
     
    if len(score_count) == False:
        print("Thanks for stopping by - \n")
        print("But when you come by next, how about giving the game a try, huh? \n")
      
    elif len(score_count) == True:
        print(f"You played {round_number} rounds ... \n")
        print(f"And, the lowest number of guesses it took you to guess correctly was {min(score_count)}. \n")
        print("Not bad, not bad at all! \n\n")
        print("Well, I guess that's all then -  Have a nice day, and hope to see you around here again!")
      

    
start_game()
    
if play_game1 == "y":
   play_round()
     
end_game()