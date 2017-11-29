import prisoner

class PrisonerFactory:
    @staticmethod
    def get_prisoner(name):
        for subclass in prisoner.Prisoner.__subclasses__():
            if subclass.get_name() == name:
                return subclass()

