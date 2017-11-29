from prisonerfactory import PrisonerFactory as PF
from ipd import PrisonersDilemma as PD
import random

from graph import TimelineGif

class Tournament:

    scores = {}
    total = 0
    timeline = []
    
    def __init__(self, prisoners, generations=25):
        self.prisoners = prisoners
        self.generations = generations
        self.scores = self.scores.fromkeys(prisoners, 0)
        self.queue = [PF.get_prisoner(k) for k, v in prisoners.items() for _ in range(v)]
        self.pop_size = len(self.queue)

    def _tournament_play(self):
        for k, p1 in enumerate(self.queue):
            for p2 in self.queue[1+k:]:
                PD(p1, p2).iterative_play()

    def _total_points(self):
        for p in self.queue:
            self.total += p.score
            self.scores[p.get_name()] += p.score

    def _cumulative(self):
        total = 0
        for p in self.scores:
            total += self.scores[p]
            self.scores[p] = total

    def _repopulate_queue(self):
        self.queue = []
        for _ in range(self.pop_size):
            rand = random.randint(0, self.total)
            for p, score in self.scores.items():
                if rand < score:
                    self.queue.append(PF.get_prisoner(p))
                    break

    def _reset(self):
        self.total = 0
        self.scores = self.scores.fromkeys(self.scores, 0)
        self.prisoners = self.prisoners.fromkeys(self.prisoners, 0)

    def _recount(self):
        for p in self.queue:
            self.prisoners[p.get_name()] += 1
        self.timeline.append(self.prisoners)

    def run_tourny(self, printing=True):
        for _ in range(self.generations):
           self._tournament_play()
           self._total_points()
           self._cumulative()
           self._repopulate_queue()
           self._reset()
           self._recount()
           if printing:
               print(self.prisoners) 
        return self.timeline
