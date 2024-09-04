#!/usr/bin/env python3

class Person:
    def __init__(self, name):
        # The __init__ method is called when an object is instantiated.
        # It initializes the instance with the provided name.
        self.name = name

    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")