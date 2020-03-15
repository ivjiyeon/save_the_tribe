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
from Soldier import Soldier


class Task4Soldier(Soldier):
    def __init__(self):
        super().__init__()
        self.coin = 0
        self.num_shield = 0
        self.defence = 0

    def get_coin(self):
        return self.coin

    def add_coin(self):
        self.coin = self.coin+1

    def get_elixir(self, merchant):
        self.coin -= merchant.get_elixir_price()
        super().add_elixir()

    def get_shield(self, merchant):
        self.coin -= merchant.get_shield_price()
        self.add_shield()
        self.set_defence()

    def set_defence(self):
        self.defence = self.num_shield * 5

    def add_shield(self):
        self.num_shield = self.num_shield + 1

    def lose_health(self):
        self.health = self.health - \
            (10 - self.defence) if self.defence <= 10 else 0
        return self.health <= 0

    def display_information(self):
        super().display_information()
        print("Defence: {}.".format(self.defence))
        print("Coin: {}.".format(self.coin))
