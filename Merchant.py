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


class Merchant():
    def __init__(self):
        self.elixir_price = 1
        self.shield_price = 2
        self.pos = Pos()

    def get_elixir_price(self):
        return self.elixir_price

    def get_shield_price(self):
        return self.shield_price

    def get_pos(self):
        return self.pos

    def set_pos(self, row, column):
        self.pos.set_pos(row, column)

    def action_on_soldier(self, soldier):
        deal_enabled = True

        while(deal_enabled):
            if(soldier.get_coin() <= 0):
                self.talk("You don't have enough coins.\n")
                deal_enabled = False
                break

            choice = input(
                "Merchant$: Do you want to buy something? (1. Elixir, 2. Shield, 3. Leave.) Input: ")

            if choice.casefold() == "1":
                soldier.get_elixir(self)
                deal_enabled = False
            elif choice.casefold() == "2":
                if soldier.get_coin() < 2:
                    self.talk("You don't have enough coins.\n")
                    deal_enabled = False
                    break
                else:
                    soldier.get_shield(self)
                    deal_enabled = False
            elif choice.casefold() == "3":
                deal_enabled = False
            else:
                print("=> Illegal choice!\n")
                break
            print()

    def talk(self, text):
        print("Merchant$: " + text)

    def display_symbol(self):
        print("$", end="")
