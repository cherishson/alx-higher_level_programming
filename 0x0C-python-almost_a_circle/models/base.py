#!/usr/bin/python3

"""

A model that contains a Base class to manage
the id attribute of allfuture  classes that extend
from Base and avoid duplicating the same code.

"""

class Base:
    """
    ...
    """
    __nb__objects = 0

    def __init__(self, id=none):

         """
        ...
        """

        if id is none:
            Base.__nb__objects += 1
            self.id = Base,__nb__objects
        else:
            self.id = id
