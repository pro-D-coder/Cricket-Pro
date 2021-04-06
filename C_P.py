class Batsman:
    def __init__(self, name =  None, j_num = None, score = 0, status = True):
        self.name = name
        self.j_num = j_num
        self.score = score
        self.status = status
    def get_score(self):
        return self.score
    def get_name(self):
        return self.name
    def get_status(self):
        return self.status
    def get_j_num(self):
        return self.j_num
    def update_score(self, to_add):
        self.score += to_add
    def change_status(self, state):
        self.status = state

class bowler:
    def __init__(self, name = None, j_num = None, runs = None, wickets = 0, over = 0, balls = 0):
        self.name = name
        self.j_num = j_num
        self.runs = runs
        self.wickets = wickets
        self.over = over
        self.balls =  balls
    def get_name(self):
        return self.name
    def get_j_num(self):
        return self.j_num