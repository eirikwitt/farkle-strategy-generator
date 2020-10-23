from collections import Counter
from itertools import product


#-----------------Generating score options--------------------------

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

#------------------------------------------------Generating all options from all dicenum-----------------------------

def combinations_generator(dice_num):
    return_combinations = Counter()
    for roll in product(range(1, 6), repeat=dice_num):
        roll = list(roll)
        roll.sort()
        roll = tuple(roll)
        return_combinations[roll]+= 1
    return return_combinations


def options_generator(dice_num):
    return_options = Counter()
    rolls = combinations_generator(dice_num)
    for roll in rolls.keys():
        options_set = []
        for option in score_options.keys():
            if not Counter(option) - Counter(roll):
                options_set.append(option)

        options_set = tuple(options_set)
        return_options[options_set] += rolls[roll]
    return return_options

def generate_options_superset():
    options = {}
    for i in range(1, 6):
        options[str(i)] = options_generator(i)
    return(options)

print(generate_options_superset())

# data = {"options": options, "score_options": score_options}
#
# with open("Options.pickle", "wb") as outfile:
#     pickle.dump(data, outfile)
