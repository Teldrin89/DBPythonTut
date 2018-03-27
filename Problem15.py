# Problem 15: small game-type-of objects - 2 warriors fighting
# each other (take turns) according to somewhat similar
# scenario (until one of them dies):
'''
Sam attacks Paul and deals 9 damage
Paul is down to 10 health
Paul attacks Sam and deals 7 damage
Sam is down to 7 health
Sam attacks Paul and deals 19 damage
Paul is down t -9 health
Paul has died and Sam is victorious
Game Over
'''
import random
import math
# Create both Warrior and Battle class
# Warriors will have names, health and attack and block maximus


class Warrior:
    # initialize a class warrior - with name, health, max
    # attack and block - 4 attributes
    def __init__(self, name="Warrior",
                 health=0, atMax=0, blMax=0):
        self.name = name
        self.health = health
        self.atMax = atMax
        self.blMax = blMax
    # They will have capabilities to attack and block -
    # 2 methods random amounts - attack random(): 0 to
    # 1 * max Attack + .5

    def attack(self):
        atAmt = self.atMax * (random.random() + .5)

        return atAmt
    # Block will use random() - similar to attack

    def block(self):
        blAmt = self.blMax * (random.random() + .5)

        return blAmt

# create a sort of utility class - it will loop
# the fight until 1 of warriors will die - create battle class


class Battle:
    # not a initialize method but a one with loop - while
    def startFight(self, warrior1, warrior2):
        # a while loop that will break in case we have a
        # game over scenario - specified later on
        while True:
            if self.getAttackResult(warrior1,
                                    warrior2) == "Game Over":
                print("Game Over")
                break

            if self.getAttackResult(warrior2,
                                    warrior1) == "Game Over":
                print("Game Over")
                break

    # the getAttackResult - a class static method - it is not
    # tied to any kind of object (doesn't need to have to refer
    # to itself - no need for "self" attribute)
    @staticmethod
    # the method will have 2 warriors as attributes - A and B
    # just to avoid confusion with 1 and 2 from previous class
    def getAttackResult(warriorA, warriorB):
        # the attack and block for each warrior is calculated
        # using methods from previous class
        warriorAAtAmt = warriorA.attack()
        warriorBBlAmt = warriorB.block()
        # damage calculated as attack - blocked value
        # using math.ceil to round numbers to integers
        damage2WarriorB = math.ceil(warriorAAtAmt -
                                    warriorBBlAmt)
        # adjustment of warrior B health after attack
        warriorB.health = warriorB.health - damage2WarriorB
        # printing out the results of the method - what happened
        # to each warrior - attack and updated health
        print("{} attacks {} and deals {} "
              "damage".format(warriorA.name, warriorB.name,
                              damage2WarriorB))
        print("{} is down to {} health".format(warriorB.name,
                                               warriorB.health))
        # Game Over scenario established - if warrior which
        # have been attacked health is below 0 - game over
        # if not then the fight continues
        if warriorB.health <= 0:
            print("{} has died and {} is "
                  "victorious".format(warriorB.name,
                                      warriorA.name))
            return "Game Over"
        else:
            return "Fight Again"


# main function to run the fight


def main():
    # definition of 2 warriors using Warrior class - specifying
    # name, max health, max attack and max block
    maximus = Warrior("Maximus", 50, 20, 10)
    galaxon = Warrior("Galaxon", 50, 20, 10)
    # definition of battle - using battle class
    battle = Battle()
    # starting of fight from battle class
    battle.startFight(maximus, galaxon)


# initialize the main function
main()
