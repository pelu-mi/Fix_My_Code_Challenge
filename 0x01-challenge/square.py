#!/usr/bin/python3
""" Module for Class Square
"""


class Square():
    """ Definition of class square
    """
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        """ Initialize the class with 2 variables """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiterofmysquare(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String representation """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiterofmysquare())
