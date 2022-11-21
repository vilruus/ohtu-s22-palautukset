class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists

    def __getItem__(self):
        return self.name, self.assists, self.team, self.goals

    def __str__(self):
        return f"{self.name:25} {self.team:1} {self.goals:3} + {self.assists:3} = {self.goals + self.assists}"