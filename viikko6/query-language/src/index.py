from statistics import Statistics
from player_reader import PlayerReader
from matchers import And,Not, HasFewerThan, HasAtLeast, All, PlaysIn

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = All()

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
