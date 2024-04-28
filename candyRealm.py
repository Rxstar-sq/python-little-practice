# <Student Name>   Yingxaun Ye          <Date it was started> 2024/4/26
# <Assignment/ Lab/ etc.> Assignment 6

import random
import colorama

def printTitleMaterial():
    """Prints the title material for the game, including the student's name, class, and section number.
    """
    print("Candy Realm!")
    print()

    print("By: Yingxuan Yw")
    print("[COM S 127 <B>]")
    print()



def main():
    board = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "White", "Brown", "Black"]
    print(board)

    n_p = int(input("Enter the number of players: "))
    player = []
    for i in range(1, n_p + 1):
        player_name = input(f"Enter name for Player {i}: ")
        player.append(player_name)
    print("Players:", player)

    game_over = False
    while not game_over:
        for p in player:
            input(f"{player}'s turn. Press Enter to draw a card...")
            drawn_card = random.choice(board)
            print(f"{p} drew {drawn_card}!")
            if drawn_card == board[-1]:
                print(f"{p} wins!")
                game_over = True
                break

if __name__ == "__main__":
    main()