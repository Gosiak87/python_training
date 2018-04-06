from random import randint


class Dice:

    DICE_TYPES = (3, 4, 6, 8, 10, 12, 20, 100)

    def __init__(self, dice_type):
        if dice_type in Dice.DICE_TYPES:
            self.dice_type = dice_type

        else:
            self.dice_type = 10

    def roll(self):
        throw = randint(1, self.dice_type)
        return throw


def roll(dice_type=3):
    dice = Dice(dice_type)
    for i in range(10):
        yield dice.roll()

#cubes = Dice(100)
#for i in range(10):
 #   print(cubes.roll())
gen = roll(12)

for result in gen:
    print(result)
