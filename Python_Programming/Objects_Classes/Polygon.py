from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def area(self):
        """returns the area"""
        pass

    @abstractmethod
    def perimeter(self):
        """return the perimeter"""
        pass
