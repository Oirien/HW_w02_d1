from team import SportsTeam

team = SportsTeam("The Weirdos",["Joe", "Jim", "John", "Jeremy"], "El Bandito")

print(team.has_player("John"))
print(team.has_player("Jimmy"))

team.add_player("Jimmy")
print(team.has_player("Jimmy"))

team.play_game(True)
print(team.points)