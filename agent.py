import random


class Agent:
    def __init__(self):
        self.pick = 0

    def agent_move(self, candies):
        if candies == 4:
            pick = 2
        else:
            pick = random.randint(1, 2)
        return pick
