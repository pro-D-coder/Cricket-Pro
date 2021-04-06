class Batsman:
    def __init__(self, name, j_num, score = 0, status = True):
        self.name = name
        self.j_num = j_num
        self.score = score
        self.status = status
    def get_score(self):
        return self.score
    def get_status(self):
        return self.status
    def get_j_num(self):
        return self.j_num
    def update_score(self, to_add):
        self.score += to_add
    def change_status(self, state):
        self.status = state

class bowler:
    def __init__(self, )