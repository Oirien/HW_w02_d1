class SportsTeam:

    def __init__(self, name, player, coach):
        self.name = name
        self.player = player
        self.coach = coach
        self.points = 0

    def add_player(self, player_name):
        self.player.append(player_name)

    def has_player(self, player2):
        for player in self.player:
            if player2 == player:
                return True
        return False
        
    def play_game(self, score):
        if score == True:
            self.points += 3