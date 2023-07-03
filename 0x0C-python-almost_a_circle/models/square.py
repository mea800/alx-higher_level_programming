#!/usr/bin/python3
"""Module that defines the Square class"""


from inspect import classify_class_attrs
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that represents a square.

     Attributes:
        width (int): width of rectangle.
        height (int): height of rectangle.
        x (int): x.
        y (int): y.
        id (int): identity of square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new Square instance

        Args:
            size (int): the size of the square
            x (int): the x-coordinate of the square's position
            y (int): the y-coordinate of the square's position
            id (int): the unique ID of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the square"""
        return ("[Square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """Gets the size of the square.

        Returns:
            int: size of one side of square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square.
        Args:
              value (int): the new size of the square
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of the square

        Args:
            *args (tuple): tuple containing the new attribute values
            **kwargs (dict): dictionary containing the new attribute values.
        """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """RReturns a dictionary representation of the squaree.

        Returns:
            dict: square.
        """
        dict1 = self.__dict__
        dict2 = {}
        dict2['id'] = dict1['id']
        dict2['size'] = dict1['_Rectangle__width']
        dict2['x'] = dict1['_Rectangle__x']
        dict2['y'] = dict1['_Rectangle__y']

        return dict2
