POINTSENUM = {
    0: 'Love',
    1: 'Fifteen',
    2: 'Thirty',
    3: 'Forty'
}

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_player1_score(self):
        return POINTSENUM[self.player1_score]

    def get_player2_score(self):
        return POINTSENUM[self.player2_score]

    def is_tie(self):
        return self.player1_score == self.player2_score

    def get_tie_score(self):
        if self.is_past_forty():
            return 'Deuce'
        else:
            return f"{self.get_player1_score()}-All"

    def is_past_forty(self):
        return self.player1_score>= 4 or self.player2_score >= 4

    def is_over(self):
        if self.is_past_forty() and abs(self.player1_score - self.player2_score) >= 2:
            return f"Win for {self.get_leader()}" 
        else:
            return self.get_advantage_score()
    
    def get_leader(self):
        if self.player1_score - self.player2_score > 0:
            return "player1"
        else: 
            return "player2"

    def get_advantage_score(self):
        return f"Advantage {self.get_leader()}"

    def get_game_score(self):
        return f"{self.get_player1_score()}-{self.get_player2_score()}"
        
    def get_score(self):
        score = ""

        if self.is_tie():
            score = self.get_tie_score()

        elif self.is_past_forty():
            score = self.is_over()

        else:
            score = self.get_game_score()

        return score
