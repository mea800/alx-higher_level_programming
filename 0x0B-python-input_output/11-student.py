#!/usr/bin/python3
"""Module defining the Student class with attributes and methods."""


class Student:
    """
    Class representing a student with first name, last name, and age.

    Attributes:
        first_name (str): The first name of the student.
        last_name (int): The last name of the student.
        age (int): The age of the student.
    """
    def __init__(self, first_name, last_name, age):
        """Constructor that initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (int): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list): Optional list of strings
                representing attribute names.
                If provided, only the specified attributes will be retrieved.
                Otherwise, all attributes will be retrieved.

        Returns:
            dict: Dictionary representation of the Student instance.
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

    def reload_from_json(self, json):
        """Updates attributes of the Student instance with a dictionary.

        Args:
            json (dict): Dictionary containing attribute-value pairs.
        """
        self.__dict__.update(json)
