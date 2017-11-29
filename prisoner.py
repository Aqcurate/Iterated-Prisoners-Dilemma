from abc import ABCMeta, abstractmethod 
from conf import choices

class Prisoner(metaclass=ABCMeta):
    def __init__(self):
        self.score = 0.0
        self.history = []

    @abstractmethod
    def get_action(self, opponent):
        pass

    @abstractmethod
    def get_name():
        pass

class TFT(Prisoner):
    def get_action(self, opponent):
        if len(opponent.history) == 0:
            return choices['COOP']
        else:
            return opponent.history[-1]

    @staticmethod
    def get_name():
        return 'Tit for Tat'

class Greedy(Prisoner):
    def get_action(self, opponent):
        return choices['DEFECT']

    @staticmethod
    def get_name():
        return 'Greedy'

