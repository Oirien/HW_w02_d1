class SportsTeam:

    def __init__(self, name, player, coach):
        self.name = name
        self.player = [player]
        self.coach = coach

    def add_player(self, name):
        self.player.append(name)

    def has_player(self, name):
        return any(self.player(name))
        