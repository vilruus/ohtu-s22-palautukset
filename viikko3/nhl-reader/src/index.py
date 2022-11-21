import requests
from operator import itemgetter
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        if player_dict['nationality'] != 'FIN':
            continue
        player = Player(
            player_dict['name'],
            player_dict['team'],
            player_dict['goals'],
            player_dict['assists']
        )
        players.append(player)

    sortedByPoints = sorted(players, key=lambda p: p.goals + p.assists, reverse=True)
    print(players)
    print("Oliot:")
    for player in sortedByPoints:
        print(player)


if __name__ == "__main__":
    main()
