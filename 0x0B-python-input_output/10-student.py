#!/usr/bin/python3
"""Module defining the Student class to represent student objects."""


class Student:
    """
    A class that represents a student with first name, last name, and age.

    Attributes:
        first_name (str): The first name of the student.
        last_name (int): The last name of the student.
        age (int): The age of the student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (int): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of a Student instance.

        If attrs is a list of strings, only the attributes with names
        contained in this list are included in the dictionary.
        Otherwise, all attributes are included.

        Args:
            attrs (list): A list of attribute names
        to include in the dictionary.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for item in attrs:
            try:
                new_dict[item] = self.__dict__[item]
            except Exception:
                pass
        return new_dict
