from os import system, name
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def set_stats(type):
    if type == "bat":
        bat_stats = batsman_stats()
        return bat_stats
    elif type == "bow":
        bowl_stats = bowler_stats()
        return bowl_stats
    else:
        all_stats = all_rounder_stats()
        return bowl_stats
class score_card:
    def __init__(self, wickets = 0, runs = 0):
        self.wickets = wickets
        self.runs = runs

class over:
    def __init__(self,balls = 0):
        self.over = str(balls//6) +"."+ str(balls%6)
    def __repr__(self):
        return self.over
class bowler_stats:
    def __init__(self, over = over(), runs_gived = 0, wickets = 0, economy = 0, runs = 0, played_bowls = 0, strike_rate = 100, status = True):
        self.over = over
        self.runs_gived = runs_gived
        self.wickets = wickets
        self.economy = economy
        self.runs = runs
        self.played_bowls = played_bowls
        self.strike_rate = strike_rate
        self.status = status
class batsman_stats:
    def __init__(self, runs = 0, played_bowls = 0, strike_rate = 100, status = True):
        self.runs = runs
        self.played_bowls = played_bowls
        self.strike_rate = strike_rate
        self.status = status
class all_rounder_stats(bowler_stats, batsman_stats):
    pass
class Player():  
    player_count = 0
    def __init__(self, j_num, name = "", type = 'bat'):  #available Types are bat: batsman, bow: bowler, all: all-rounder.
        self.name = name
        self.j_num = j_num
        self.type = type
        self.stats = set_stats(type)
    def __str__(self):
        return self.name
class Team():
    NUMBER_OF_TEAMS = 0
    def __init__(self, id = NUMBER_OF_TEAMS+1, name = "", n_members = 11, ):
        Team.NUMBER_OF_TEAMS += 1
        self.team_id = id
        self.team_name = name
        self.n_team_members = n_members
        self.team_members = list()
        self.striker = self.team_members[0]
        self.non_striker = self.team_members[1]
    def __repr__(self):
        return self.team_name
    def get_team_name(self):
        return self.team_name
    def get_n_member(self):
        return self.n_team_members
    def take_players_name(self):
        print("Enter Player Detail Inorder they bat: ")
        for i in range(1, self.n_team_members+1):
            player =  Player(j_num = input("Enter player jersey number: "), name = input("Enter {0} player name: ".format(i)), type = input("Enter Player Type(bat/bow/all): "))
            self.team_members.append(player)
    def get_all_bowlers(self):
        all_player = self.team_members
        avail_bowl = [i for i in all_player if i.type == "bow"]
        return avail_bowl

def display(match):
    clear()
    print("Team: {0}", match.team1.team_name)
    print("Score: {0} / {1}\n".format(match.score_card.runs, match.score_card.wickets))
    print("Over: {0}".format(match.over))
    print("Batsman:  {0}  {1}({2})\t\t{3} {4}({5})".format(match.team1.striker.name,
    match.team1.striker.stats.runs,
    match.team1.striker.stats.played_bowls,
    match.team1.striker.stats.strike_point,
    match.team2.striker.name,
    match.team2.striker.stats.runs,
    match.team2.striker.stats.played_bowls,
    match.team2.striker.stats.strike_point))
    print("Choose Bowler: ")
    for j i in enumerate(match.team2.get_all_bowlers()):
        print("{0}. {1}".format(j+1,i.name))
    int(input("Enter Choice: "))
    print("Bowler: {0}-{1}({2})".format())
    

class Cricket():
    def __init__(self, total_overs = over(), score = score_card(), teamA, teamB):
        self.over = total_overs
        self.score_card = score
        self.team1 = teamA
        self.team2 = teamB

print("***************************WEL-COME IN CRICKET BOARD*****************************")
teamA = Team(name = input("Enter First Team Name: "), n_members= int(input("Enter Number Of Team Members: ")))
teamA.take_players_name()
teamB = Team(name = input("Enter Second Team Name: "), n_members= int(input("Enter Number Of Team Members: ")))
teamB.take_players_name()
match = Cricket(over(balls=  int(input("Enter Number Of Balls To Be Played Per Inning: "))), score = score_card(), teamA, teamB)
display(match)