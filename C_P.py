class bowler_stats:
    def __init__(self, over = 0, balls = 0, runs_gived = 0, wickets = 0):
        self.over = over
        self.balls = balls
        self.runs_gived = runs_gived
        self.wickets = wickets

class batsman_stats:
    def __init__(self, runs = 0, played_bowls = 0, strike_rate = 100, status = True):
        self.runs = runs
        self.played_bowls = played_bowls
        self.strike_rate = strike_rate
        self.status = status

class Player(bowler_stats, batsman_stats):
    player_count = 0
    def __init__(self, name, j_num):
        self.name = name
        self.j_num = j_num
        self.team = Team()

class Team(Bowler, Batsman):
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
    def get_players_name(self):
        for i in range(1, self.n_team_members+1):
            self.team_members.append(input("Enter {0} Player Name: ".format(i)))

class Cricket(Team):
    def __init__(self):
        print("\t\t*********************WEL-COME TO CRICKET BOARD******************")
        self.teamA =  super().__init__(name = input("Enter First Team Name: "), n_members= int(input('Enter Number of Members: ')))
        self.teamB = super().__init__(name= input('Enter Second Team Name: '), n_members=int(input("Enter Number of Members: ")))        
match = Cricket()