#!/usr/bin/env python3


class Dog:
    def __init__(self, name, breed="Mutt"):
        # The __init__ method is called when an object is instantiated.
        # It initializes the instance with the provided name and breed.
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")

