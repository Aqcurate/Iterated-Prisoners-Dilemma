from conf import choices, points
from prisonerfactory import PrisonerFactory
import random

class PrisonersDilemma:
    
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play(self):
        action1 = self.p1.get_action(p2)
        action2 = self.p2.get_action(p1)

        self.p1.history.append(action1)
        self.p2.history.append(action2)

        if action1 == choices['COOP']:
            if action2 == choices['COOP']:
                # CC
                self.p1.score += points['REWARD']
                self.p2.score += points['REWARD']
            else:
                # CD
                self.p1.score += points['SUCKER']
                self.p2.score += points['TEMPTATION']
        else:
            if action2 == choices['COOP']:
                # DC
                self.p1.score += points['TEMPTATION']
                self.p2.score += points['SUCKER']
            else:
                # DD
                self.p1.score += points['PUNISHMENT']
                self.p2.score += points['PUNISHMENT']
    
    def iterative_play(self, range_min, range_max):
        
        num = random.randint(range_min, range_max)

        for k in range(num):
            self.play()

        self.reset_history()

        self.p1.score /= num
        self.p2.score /= num

    def reset_history(self):
        p1.history = []
        p2.history = []


p1 = PrisonerFactory.get_prisoner('Tit for Tat')
p2 = PrisonerFactory.get_prisoner('Greedy')
c = PrisonersDilemma(p1, p2)
c.iterative_play(100, 200)

print(p1.score)
print(p2.score)

