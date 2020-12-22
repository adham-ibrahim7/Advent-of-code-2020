f = open("../inputs/day22.txt")

player1, player2 = [list(map(int, player.split("\n")[1:])) for player in f.read().split("\n\n")]


def move(winner, loser):
    return winner[1:] + [winner[0]] + [loser[0]], loser[1:]


def winner_p1(player1, player2):
    while len(player1) > 0 and len(player2) > 0:
        if player1[0] > player2[0]:
            player1, player2 = move(player1, player2)
        else:
            player2, player1 = move(player2, player1)
    return player1 if len(player1) != 0 else player2


winner = winner_p1(player1, player2)
print("p1:", sum((card * (len(winner) - i)) for i, card in enumerate(winner)))


def hash_players(player1, player2):
    return (tuple(player1), tuple(player2)).__hash__()


def winner_of_round(player1, player2):
    if player1[0] <= len(player1)-1 and player2[0] <= len(player2)-1:
        return winner_of_game(player1[1:player1[0]+1], player2[1:player2[0]+1])[0]
    return 1 if player1[0] > player2[0] else 2


def winner_of_game(player1, player2):
    past_games = set()
    while len(player1) > 0 and len(player2) > 0:
        # print("round:", round, player1, player2)
        if hash_players(player1, player2) in past_games or winner_of_round(player1, player2) == 1:
            temp1, temp2 = move(player1, player2)
        else:
            temp2, temp1 = move(player2, player1)
        past_games.add(hash_players(player1, player2))
        player1, player2 = temp1, temp2

    if len(player1) == 0:
        return 2, player2
    else:
        return 1, player1


_, winner = winner_of_game(player1, player2)
print("p2:", sum((card * (len(winner) - i)) for i, card in enumerate(winner)))
