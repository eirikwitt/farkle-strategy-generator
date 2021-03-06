from collections import Counter
from itertools import product
import pickle


#-----------------Generating score options--------------------------

# Score options are all possible options a player can choose that gives points.

# Function adds combinations of existing score options to 
def score_options_generator(previous_options):
    options_dices_temp = dict()
    for op1 in previous_options.keys():
        options_dices_temp[op1] = previous_options[op1]
        for op2 in previous_options.keys():
            if len(op1) + len(op2) <= 6:
                op3 = op1 + op2
                op3 = sorted(op3)
                op3 = tuple(op3)
                if op3 not in options_dices_temp:
                    options_dices_temp[op3] = previous_options[op1] + previous_options[op2]
    return options_dices_temp


score_options = {
    tuple([1]):100, (1, 1):200, (1, 1, 1):1000, (1, 1, 1, 1):2000, (1, 1, 1, 1, 1):3000, (1, 1, 1, 1, 1, 1):4000,
    (2, 2, 2):200, (2, 2, 2, 2):400, (2, 2, 2, 2, 2):600, (2, 2, 2, 2, 2, 2):800,
    (3, 3, 3):300, (3, 3, 3, 3):600, (3, 3, 3, 3, 3):900, (3, 3, 3, 3, 3, 3):1200,
    (4, 4, 4):400, (4, 4, 4, 4):800, (4, 4, 4, 4, 4):1200, (4, 4, 4, 4, 4, 4):1600,
    tuple([5]):50, (5, 5):100 ,(5, 5, 5):500, (5, 5, 5, 5):1000, (5, 5, 5, 5, 5):1500, (5, 5, 5, 5, 5, 5):2000,
    (6, 6, 6):600, (6, 6, 6, 6):1200, (6, 6, 6, 6, 6):1800, (6, 6, 6, 6, 6, 6):2400, (1, 2, 3, 4, 5, 6):1500,
    (1, 1, 2, 2, 3, 3):750, (1, 1, 2, 2, 4, 4):750, (1, 1, 2, 2, 5, 5):750, (1, 1, 2, 2, 6, 6):750,
    (1, 1, 3, 3, 4, 4):750, (1, 1, 3, 3, 5, 5):750, (1, 1, 3, 3, 6, 6):750, (1, 1, 4, 4, 5, 5):750,
    (1, 1, 4, 4, 6, 6):750, (1, 1, 5, 5, 6, 6):750, (2, 2, 3, 3, 4, 4):750, (2, 2, 3, 3, 5, 5):750,
    (2, 2, 3, 3, 6, 6):750, (2, 2, 4, 4, 5, 5):750, (2, 2, 4, 4, 6, 6):750, (2, 2, 5, 5, 6, 6):750,
    (3, 3, 4, 4, 5, 5):750, (3, 3, 4, 4, 6, 6):750, (3, 3, 5, 5, 6, 6):750, (4, 4, 5, 5, 6, 6):750,
}

while True:
    score_options_new = score_options_generator(score_options)
    if score_options_new == score_options:
        break
    score_options = score_options_new

print(score_options)
print()

#------------------------------------------------Generating all options from all dicenum-----------------------------

def combinations_generator(dice_num):
    return_combinations = dict()
    for roll in product([1, 2, 3, 4, 5, 6], repeat=dice_num):
        roll = list(roll)
        roll.sort()
        roll = tuple(roll)
        if roll in return_combinations:
            return_combinations[roll]+= 1
        else:
            return_combinations[roll] = 1
    return return_combinations


def options_generator(dice_num):
    return_options = dict()
    rolls = combinations_generator(dice_num)
    for roll in rolls.keys():
        options_set = []
        for option in score_options.keys():
            if not Counter(option) - Counter(roll):
                options_set.append(option)

        options_set = tuple(options_set)
        if options_set in return_options:
            return_options[options_set] += rolls[roll]
        else:
            return_options[options_set] = rolls[roll]
    return return_options

options = {}
for i in range(1, 6):
    options[str(i)] = options_generator(i)
print(options)

# data = {"options": options, "score_options": score_options}
#
# with open("Options.pickle", "wb") as outfile:
#     pickle.dump(data, outfile)






# {'1': {((1,),): 1, (): 4, ((5,),): 1}, '2': {((1,), (1, 1)): 1, ((1,),): 8, ((1,), (1, 5), (5,)): 2, (): 16, ((5,),): 8, ((5,), (5, 5)): 1}, '3': {((1,), (1, 1), (1, 1, 1)): 1, ((1,), (1, 1)): 12, ((1,), (1, 1), (1, 1, 5), (1, 5), (5,)): 3, ((1,),): 48, ((1,), (1, 5), (5,)): 24, ((1,), (1, 5), (1, 5, 5), (5,), (5, 5)): 3, ((2, 2, 2),): 1, (): 60, ((5,),): 48, ((5,), (5, 5)): 12, ((3, 3, 3),): 1, ((4, 4, 4),): 1, ((5,), (5, 5), (5, 5, 5)): 1, ((6, 6, 6),): 1}, '4': {((1,), (1, 1), (1, 1, 1), (1, 1, 1, 1)): 1, ((1,), (1, 1), (1, 1, 1)): 16, ((1,), (1, 1), (1, 1, 1), (1, 1, 5), (1, 1, 1, 5), (1, 5), (5,)): 4, ((1,), (1, 1)): 96, ((1,), (1, 1), (1, 1, 5), (1, 5), (5,)): 48, ((1,), (1, 1), (1, 1, 5), (1, 1, 5, 5), (1, 5), (1, 5, 5), (5,), (5, 5)): 6, ((1,), (1, 2, 2, 2), (2, 2, 2)): 4, ((1,),): 240, ((1,), (1, 5), (5,)): 192, ((1,), (1, 5), (1, 5, 5), (5,), (5, 5)): 48, ((1,), (1, 3, 3, 3), (3, 3, 3)): 4, ((1,), (1, 4, 4, 4), (4, 4, 4)): 4, ((1,), (1, 5), (1, 5, 5), (1, 5, 5, 5), (5,), (5, 5), (5, 5, 5)): 4, ((1,), (1, 6, 6, 6), (6, 6, 6)): 4, ((2, 2, 2), (2, 2, 2, 2)): 1, ((2, 2, 2),): 12, ((2, 2, 2), (2, 2, 2, 5), (5,)): 4, (): 204, ((5,),): 240, ((5,), (5, 5)): 96, ((3, 3, 3),): 12, ((4, 4, 4),): 12, ((5,), (5, 5), (5, 5, 5)): 16, ((6, 6, 6),): 12, ((3, 3, 3), (3, 3, 3, 3)): 1, ((3, 3, 3), (3, 3, 3, 5), (5,)): 4, ((4, 4, 4), (4, 4, 4, 4)): 1, ((4, 4, 4), (4, 4, 4, 5), (5,)): 4, ((5,), (5, 5), (5, 5, 5), (5, 5, 5, 5)): 1, ((5,), (5, 6, 6, 6), (6, 6, 6)): 4, ((6, 6, 6), (6, 6, 6, 6)): 1}, '5': {((1,), (1, 1), (1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1, 1)): 1, ((1,), (1, 1), (1, 1, 1), (1, 1, 1, 1)): 20, ((1,), (1, 1), (1, 1, 1), (1, 1, 1, 1), (1, 1, 5), (1, 1, 1, 5), (1, 1, 1, 1, 5), (1, 5), (5,)): 5, ((1,), (1, 1), (1, 1, 1)): 160, ((1,), (1, 1), (1, 1, 1), (1, 1, 5), (1, 1, 1, 5), (1, 5), (5,)): 80, ((1,), (1, 1), (1, 1, 1), (1, 1, 5), (1, 1, 5, 5), (1, 1, 1, 5), (1, 1, 1, 5, 5), (1, 5), (1, 5, 5), (5,), (5, 5)): 10, ((1,), (1, 1), (1, 1, 2, 2, 2), (1, 2, 2, 2), (2, 2, 2)): 10, ((1,), (1, 1)): 600, ((1,), (1, 1), (1, 1, 5), (1, 5), (5,)): 480, ((1,), (1, 1), (1, 1, 5), (1, 1, 5, 5), (1, 5), (1, 5, 5), (5,), (5, 5)): 120, ((1,), (1, 1), (1, 1, 3, 3, 3), (1, 3, 3, 3), (3, 3, 3)): 10, ((1,), (1, 1), (1, 1, 4, 4, 4), (1, 4, 4, 4), (4, 4, 4)): 10, ((1,), (1, 1), (1, 1, 5), (1, 1, 5, 5), (1, 1, 5, 5, 5), (1, 5), (1, 5, 5), (1, 5, 5, 5), (5,), (5, 5), (5, 5, 5)): 10, ((1,), (1, 1), (1, 1, 6, 6, 6), (1, 6, 6, 6), (6, 6, 6)): 10, ((1,), (1, 2, 2, 2), (1, 2, 2, 2, 2), (2, 2, 2), (2, 2, 2, 2)): 5, ((1,), (1, 2, 2, 2), (2, 2, 2)): 60, ((1,), (1, 2, 2, 2), (1, 2, 2, 2, 5), (1, 5), (2, 2, 2), (2, 2, 2, 5), (5,)): 20, ((1,),): 1020, ((1,), (1, 5), (5,)): 1200, ((1,), (1, 5), (1, 5, 5), (5,), (5, 5)): 480, ((1,), (1, 3, 3, 3), (3, 3, 3)): 60, ((1,), (1, 4, 4, 4), (4, 4, 4)): 60, ((1,), (1, 5), (1, 5, 5), (1, 5, 5, 5), (5,), (5, 5), (5, 5, 5)): 80, ((1,), (1, 6, 6, 6), (6, 6, 6)): 60, ((1,), (1, 3, 3, 3), (1, 3, 3, 3, 3), (3, 3, 3), (3, 3, 3, 3)): 5, ((1,), (1, 3, 3, 3), (1, 3, 3, 3, 5), (1, 5), (3, 3, 3), (3, 3, 3, 5), (5,)): 20, ((1,), (1, 4, 4, 4), (1, 4, 4, 4, 4), (4, 4, 4), (4, 4, 4, 4)): 5, ((1,), (1, 4, 4, 4), (1, 4, 4, 4, 5), (1, 5), (4, 4, 4), (4, 4, 4, 5), (5,)): 20, ((1,), (1, 5), (1, 5, 5), (1, 5, 5, 5), (1, 5, 5, 5, 5), (5,), (5, 5), (5, 5, 5), (5, 5, 5, 5)): 5, ((1,), (1, 5), (1, 5, 6, 6, 6), (1, 6, 6, 6), (5,), (5, 6, 6, 6), (6, 6, 6)): 20, ((1,), (1, 6, 6, 6), (1, 6, 6, 6, 6), (6, 6, 6), (6, 6, 6, 6)): 5, ((2, 2, 2), (2, 2, 2, 2), (2, 2, 2, 2, 2)): 1, ((2, 2, 2), (2, 2, 2, 2)): 15, ((2, 2, 2), (2, 2, 2, 5), (2, 2, 2, 2), (2, 2, 2, 2, 5), (5,)): 5, ((2, 2, 2),): 90, ((2, 2, 2), (2, 2, 2, 5), (5,)): 60, ((2, 2, 2), (2, 2, 2, 5), (2, 2, 2, 5, 5), (5,), (5, 5)): 10, ((3, 3, 3),): 90, (): 600, ((5,),): 1020, ((5,), (5, 5)): 600, ((4, 4, 4),): 90, ((5,), (5, 5), (5, 5, 5)): 160, ((6, 6, 6),): 90, ((3, 3, 3), (3, 3, 3, 3)): 15, ((3, 3, 3), (3, 3, 3, 5), (5,)): 60, ((4, 4, 4), (4, 4, 4, 4)): 15, ((4, 4, 4), (4, 4, 4, 5), (5,)): 60, ((5,), (5, 5), (5, 5, 5), (5, 5, 5, 5)): 20, ((5,), (5, 6, 6, 6), (6, 6, 6)): 60, ((6, 6, 6), (6, 6, 6, 6)): 15, ((3, 3, 3), (3, 3, 3, 3), (3, 3, 3, 3, 3)): 1, ((3, 3, 3), (3, 3, 3, 5), (3, 3, 3, 3), (3, 3, 3, 3, 5), (5,)): 5, ((3, 3, 3), (3, 3, 3, 5), (3, 3, 3, 5, 5), (5,), (5, 5)): 10, ((4, 4, 4), (4, 4, 4, 4), (4, 4, 4, 4, 4)): 1, ((4, 4, 4), (4, 4, 4, 5), (4, 4, 4, 4), (4, 4, 4, 4, 5), (5,)): 5, ((4, 4, 4), (4, 4, 4, 5), (4, 4, 4, 5, 5), (5,), (5, 5)): 10, ((5,), (5, 5), (5, 5, 5), (5, 5, 5, 5), (5, 5, 5, 5, 5)): 1, ((5,), (5, 5), (5, 5, 6, 6, 6), (5, 6, 6, 6), (6, 6, 6)): 10, ((5,), (5, 6, 6, 6), (5, 6, 6, 6, 6), (6, 6, 6), (6, 6, 6, 6)): 5, ((6, 6, 6), (6, 6, 6, 6), (6, 6, 6, 6, 6)): 1}}
