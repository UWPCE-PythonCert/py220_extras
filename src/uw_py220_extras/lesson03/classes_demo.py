import math

class Pizza():
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    @staticmethod
    def compute_area(radius):
        """Static methods are a special case of methods. Sometimes,
           you'll write code that belongs to a class, but that doesn't
           use the object itself at all."""

        return math.pi * (radius ** 2)

    @classmethod
    def compute_volume(cls, height, radius):
        """Class methods are methods that are
           not bound to an object, but to a class"""

        return height * cls.compute_area(radius)


    def get_volume(self):
        return self.compute_volume(self.height, self.radius)
