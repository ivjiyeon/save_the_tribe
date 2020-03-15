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

from Monster import Monster
from Soldier import Soldier
from Spring import Spring
from Pos import Pos
from Cell import Cell


class Map():
    def __init__(self):
        self.cells = [[Cell() for i in range(7)] for j in range(7)]

    def add_object(self, object):
        pos = Pos()

        try:
            for monster in object:
                pos = monster.get_pos()
                self.cells[pos.get_row() - 1][pos.get_column() -
                                              1].set_occupied_object(monster)
        except:
            pos = object.get_pos()

            if pos != None:
                self.cells[pos.get_row() - 1][pos.get_column() -
                                              1].set_occupied_object(object)

    def display_map(self):
        print("   | 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
        print("--------------------------------")

        for i in range(7):
            print(" {} |".format(i + 1), end='')
            for j in range(7):
                occupied_object = self.cells[i][j].get_occupied_object()
                if occupied_object != None:
                    print(" ", end='')
                    occupied_object.display_symbol()
                    print(" |", end='')
                else:
                    print("   |", end='')
            print("")
            print("--------------------------------")
        print()

    def get_occupied_object(self, row, column):
        return self.cells[row - 1][column - 1].get_occupied_object()

    def check_move(self, row, column):
        return (1 <= row <= 7) and (1 <= column <= 7)

    def update(self, soldier, old_row, old_column, new_row, new_column):
        self.cells[old_row - 1][old_column - 1].set_occupied_object(None)
        self.cells[new_row - 1][new_column - 1].set_occupied_object(soldier)
