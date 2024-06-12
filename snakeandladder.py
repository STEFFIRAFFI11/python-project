import random 

snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

def roll_dice():
    return random.randint(1, 6)

def move_player(player_position, dice_value):
    player_position += dice_value
    
    if player_position in snakes:
        print(f"Oops! Bitten by a snake at {player_position}. Go down to {snakes[player_position]}")
        player_position = snakes[player_position]
    elif player_position in ladders:
        print(f"Yay! Climbed a ladder at {player_position}. Go up to {ladders[player_position]}")
        player_position = ladders[player_position]

    return player_position

def play_game():
    player1_position = 0
    player2_position = 0
    turn = 1

    while player1_position < 100 and player2_position < 100:
        if turn % 2 != 0:
            print("Player 1's turn")
            dice_value = roll_dice()
            print(f"Player 1 rolled a {dice_value}")
            player1_position = move_player(player1_position, dice_value)
            print(f"Player 1 is now on square {player1_position}")
            if player1_position >= 100:
                print("Player 1 wins!")
                break
        else:
            print("Player 2's turn")
            dice_value = roll_dice()
            print(f"Player 2 rolled a {dice_value}")
            player2_position = move_player(player2_position, dice_value)
            print(f"Player 2 is now on square {player2_position}")
            if player2_position >= 100:
                print("Player 2 wins!")
                break
        
        turn += 1

if __name__== "main":
    play_game()

