class bowler_stats:
    def __init__(self, over = 0, balls = 0, runs_gived = 0, wickets = 0, economy = 0):
        self.over = over
        self.balls = balls
        self.runs_gived = runs_gived
        self.wickets = wickets
        self.economy = economy
class batsman_stats:
    def __init__(self, runs = 0, played_bowls = 0, strike_rate = 100, status = True):
        self.runs = runs
        self.played_bowls = played_bowls
        self.strike_rate = strike_rate
        self.status = status
class all_rounder_stats(bowler_stats, batsman_stats):
    pass
class Player(all_rounder_stats):  
    player_count = 0
    def __init__(self, j_num, name = "", type = 'bat'):  #available Types are bat: batsman, bow: bowler, all: all-rounder.
        self.name = name
        self.j_num = j_num
        self.type = type
    def __str__(self):
        return self.name
class Team():
    NUMBER_OF_TEAMS = 0
    def __init__(self, id = NUMBER_OF_TEAMS+1, name = "Player", n_members = 11, ):
        Team.NUMBER_OF_TEAMS += 1
        self.team_id = id
        self.team_name = name
        self.n_team_members = n_members
        self.team_members = list()
    def __repr__(self):
        return self.team_name
    def get_team_name(self):
        return self.team_name
    def get_n_member(self):
        return self.n_team_members
    def take_players_name(self):
        print("Enter Player Name Inorder they bat: ")
        for i in range(1, self.n_team_members+1):
            player =  Player(name = input("Enter {0} player name: ".format(i)), j_num = input("Enter player jersey number: "), input("Enter Player Type(bat/bow/all): "))
            self.team_members.append(player)

class Cricket():
    def __init__(self):
        print("\t\t*********************WEL-COME TO CRICKET BOARD******************")
        self.teamA = Team(name = input("Enter First Team Name: "), n_members= int(input('Enter Number of Members: ')))
        self.teamA.take_players_name()
        self.teamB = Team(name = input("Enter First Team Name: "), n_members= int(input('Enter Number of Members: ')))
        self.teamB.take_players_name()

        

match = Cricket()