from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, odegda):
        self.odegda = odegda

    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption


class Coat(Clothes):
    @property
    def consumption(self):
        print(f"Расход ткани на пальто - {round(self.odegda / 6.5) + 0.5}")
        return round(self.odegda / 6.5) + 0.5


class Costume(Clothes):
    @property
    def consumption(self):
        print(f"Расход ткани на костюм - {2 * self.odegda + 0.3}")
        return 2 * self.odegda + 0.3


coat = Coat(50)
costume = Costume(150)
print(coat + costume)
