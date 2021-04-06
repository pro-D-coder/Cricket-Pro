class Batsman:
    def __init__(self, Team, name =  None, j_num = None, score = 0, status = True, played_bowls = 0):
        self.bat_name = name
        self.bat_j_num = j_num
        self.score = score
        self.status = status
        self.played_bowls = played_bowls
        self.bat_Team = Team
    def get_score(self):
        return self.score
    def get_bat_Team(self):
        return self.bat_Team
    def get_played_bowls(self):
        return self.played_bowls
    def get_name(self):
        return self.bat_name
    def get_status(self):
        return self.status
    def get_j_num(self):
        return self.bat_j_num
    def update_score(self, to_add = 1):
        self.score += to_add
    def change_status(self, state):
        self.status = state

class Bowler:
    def __init__(self, Team, name = None, j_num = None, runs_gived = None, wickets = 0, over = 0, balls = 0):
        self.bow_name = name
        self.bow_j_num = j_num
        self.runs_gived = runs_gived
        self.wickets = wickets
        self.bow_over = over
        self.bow_balls =  balls
        self.bow_Team = Team
    def get_bow_name(self):
        return self.bow_name
    def get_bow_Team(self):
        return self.Team
    def get_bow_j_num(self):
        return self.bow_j_num
    def get_runs_gived(self):
        return self.runs_gived
    def get_wickets(self):
        return self.wickets
    def get_bow_over(self):
        return self.bow_over
    def get_bow_balls(self):
        return self.bow_balls
    def update_runs_gived(self, runs = 1):
        self.runs_gived += runs
    def update_wickets(self, wickets = 1):
        self.wickets += wickets
    def update_overs(self, overs = 1):
        self.bow_over += overs
    def update_balls(self, ball = 1):
        self.bow_balls += balls

class Team(Bowler, Batsman):
    NUMBER_OF_TEAMS = 0
    def __init__(self, id = NUMBER_OF_TEAMS+1, name = None, n_members = 11):
        Team.NUMBER_OF_TEAMS += 1
        self.team_id = id
        self.team_name = name
        self.n_team_members = n_members
    def __repr__(self):
        return self.team_name
    def get_team_name(self):
        return self.team_name
    def get_n_member(self):
        return self.n_team_members