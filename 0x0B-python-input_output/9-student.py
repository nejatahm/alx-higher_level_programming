#!/usr/bin/python3
"""
contains the class "Student"
"""


class Student:
    """Reprsentation of a student"""
    def __init__(self,first_name,last_name,age):
        """intializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retursns a dictionary reprsentation of a Student instance"""
        return self.__dict__
