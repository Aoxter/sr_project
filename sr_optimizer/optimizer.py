

class optimizer:
    def __init__(self, NPM, seed, UCB_beta):
        self.next_day_data = None
        self.NPM = NPM
        self.seed = seed
        self.UCB_beta = UCB_beta

    def next_day(self, next_day_data):
        None