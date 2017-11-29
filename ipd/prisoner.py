from .conf import choices
from abc import ABCMeta, abstractmethod 

class Prisoner(metaclass=ABCMeta):
    def __init__(self):
        self.score = 0.0
        self.avg_score = 0.0
        self.history = []

    @staticmethod
    def get_prisoner(name):
        for subclass in Prisoner.__subclasses__():
            if subclass.get_name() == name:
                return subclass()

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

class Nice(Prisoner):
    def get_action(self, opponent):
        return choices['COOP']

    @staticmethod
    def get_name():
        return 'Nice'

class Spiteful(Prisoner):
    def get_action(self, opponent):
        if choices['DEFECT'] in opponent.history:
            return choices['DEFECT']
        else:
            return choices['COOP']

    @staticmethod
    def get_name():
        return 'Spiteful'
