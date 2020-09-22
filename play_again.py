def get_play_again():
    play_again = None
    while play_again != "y" and play_again != "n":
        play_again = input("Would you like to play again? [y/n]: ").lower()

    return play_again
    print(f"The user entered: {get_play_again()}")



get_play_again()