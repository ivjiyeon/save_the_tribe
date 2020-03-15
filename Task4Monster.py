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


class Task4Monster(Monster):
    def __init__(self, monster_id, health_capacity):
        super().__init__(monster_id, health_capacity)

    def fight(self, soldier):
        fight_enabled = True

        while fight_enabled:
            print("       | Monster{} | Soldier |".format(self.monster_id))
            print("Health | {0:8d} | {1:7d} |\n".format(
                self.health, soldier.get_health()))
            choice = input(
                "=> What is the next step? (1 = Attack, 2 = Escape, 3 = Use Elixir.) Input: ")
            if choice.casefold() == "1":
                if self.lose_health():
                    print("=> You defeated Monster{}.\n".format(self.monster_id))
                    self.drop_items(soldier)
                    soldier.add_coin()
                    fight_enabled = False

                else:
                    if soldier.lose_health():
                        self.recover(self.health_capacity)
                        fight_enabled = False

            elif choice.casefold() == "2":
                self.recover(self.health_capacity)
                fight_enabled = False

            elif choice.casefold() == "3":
                if soldier.get_num_elixirs() == 0:
                    print("=> You have run out of elixirs.\n")
                else:
                    soldier.use_elixir()

            else:
                print("=> Illegal choice!\n")
