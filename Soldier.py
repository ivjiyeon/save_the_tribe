####################################################33########################
#  CSCI3180 Principles of Programming Languages

#  --- Declaration ---

#  I declare that the assignment here submitted is original except for source
#  material explicitly acknowledged. I also acknowledge that I am aware of
#  University policy and regulations on honesty in academic work, and of the
#  disciplinary guidelines and procedures applicable to breaches of such policy
#  and regulations, as contained in the website
#  http://www.cuhk.edu.hk/policy/academichonesty/

#  Assignment 2
#  Name : Byun Jiyeon
#  Student ID : 1155086596
#  Email Addr : ivjiyeon@link.cuhk.edu.hk
###############################################################################

from Pos import Pos
from random import randint


class Soldier():
    def __init__(self):
        self.health = 100
        self.num_elixir = 2
        self.pos = Pos()
        self.keys = set([])

    def get_health(self):
        return self.health

    def lose_health(self):
        self.health = self.health - 10
        return self.health <= 0

    def recover(self, healing_power):
        total_health = healing_power + self.health
        self.health = 100 if total_health >= 100 else total_health

    def get_pos(self):
        return self.pos

    def set_pos(self, row, column):
        return self.pos.set_pos(row, column)

    def move(self, row, column):
        self.set_pos(row, column)

    def get_keys(self):
        return self.keys

    def add_key(self, key):
        self.keys.add(key)

    def get_num_elixirs(self):
        return self.num_elixir

    def add_elixir(self):
        self.num_elixir = self.num_elixir + 1

    def use_elixir(self):
        self.recover(randint(0, 6) + 15)
        self.num_elixir = self.num_elixir - 1

    def display_information(self):
        print("Health: {}.".format(self.health))
        print("Position (row, column): ({}, {}).".format(
            self.pos.get_row(), self.pos.get_column()))
        print("Keys: " + str(list(self.keys)) + ".")
        print("Elixirs: {}.".format(self.num_elixir))

    def display_symbol(self):
        print("S", end="")
