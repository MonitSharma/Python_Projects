import numpy


def game(winning_door, selected_door, change=False):
    assert winning_door < 3
    assert winning_door >= 0

    # Presenter removes the first door that was not selected neither winning
    removed_door = next(i for i in range(3) if i != selected_door and i != winning_door)

    # Player decides to change its choice
    if change:
        selected_door = next(i for i in range(3) if i != selected_door and i != removed_door)

    # We suppose the player never wants to change its initial choice.
    return selected_door == winning_door


if __name__ == '__main__':
    player_doors = numpy.random.random_integers(0, 2, (1000 * 1000 * 1,))

    winning_doors = [d for d in player_doors if game(1, d)]
    print("Winning percentage without changing choice: ", len(winning_doors) / len(player_doors))

    winning_doors = [d for d in player_doors if game(1, d, change=True)]
    print("Winning percentage while changing choice: ", len(winning_doors) / len(player_doors))
