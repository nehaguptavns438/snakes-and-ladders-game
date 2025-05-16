import random

# Snake and ladder mappings
snakes = {
    16: 6, 47: 26, 49: 11, 56: 53,
    62: 19, 64: 60, 87: 24, 93: 73,
    95: 75, 98: 78
}

ladders = {
    1: 38, 4: 14, 9: 31, 21: 42,
    28: 84, 36: 44, 51: 67, 71: 91,
    80: 100
}

player_positions = {"Player 1": 0, "Player 2": 0}


def roll_dice():
    return random.randint(1, 6)


def move_player(player):
    input(f"{player}, press Enter to roll the dice...")
    dice = roll_dice()
    print(f"{player} rolled a {dice}")

    old_position = player_positions[player]
    new_position = old_position + dice

    if new_position > 100:
        print(f"{player} needs exact roll to reach 100. Staying at {old_position}")
        return

    if new_position in snakes:
        print(f"Oh no! {player} got bitten by a snake from {new_position} to {snakes[new_position]}")
        new_position = snakes[new_position]
    elif new_position in ladders:
        print(f"Yay! {player} climbed a ladder from {new_position} to {ladders[new_position]}")
        new_position = ladders[new_position]
    else:
        print(f"{player} moved to {new_position}")

    player_positions[player] = new_position


def check_winner(player):
    if player_positions[player] == 100:
        print(f"\n🎉🎉 {player} wins the game! 🎉🎉")
        return True
    return False


def play_game():
    print("Welcome to Snakes and Ladders!\n")
    while True:
        for player in player_positions:
            move_player(player)
            if check_winner(player):
                return


if __name__ == "__main__":
    play_game()
