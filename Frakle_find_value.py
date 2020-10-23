from collections import Counter
from itertools import product

value = 0

def best_choice(dice_set, score, levels, wants_choice):
    levels -= 1
    return_score = -score
    return_choice = "There is no choice"
    for i in options_dices.keys():
        if not Counter(i) - Counter(dice_set):
            print(dice_set, i)
            if levels > 0:
                temp_score = options_dices[i] + score_from_dice_num(dice_num_generator(i, len(dice_set)), score, levels, 0)
            else:
                temp_score = options_dices[i]
            if temp_score > return_score:
                return_score = temp_score
                return_choice = i

    if wants_choice == 1:
        return return_choice
    else:
        return return_score


def options_generator():
    options_dices_temp = dict()
    for op1 in options_dices.keys():
        options_dices_temp[op1] = options_dices[op1]
        for op2 in options_dices.keys():
            if len(op1) + len(op2) < 7:
                op3 = op1 + op2
                op3 = sorted(op3)
                op3 = tuple(op3)
                if op3 not in options_dices_temp:
                    #print(op3)
                    options_dices_temp[op3] = options_dices[op1] + options_dices[op2]
    return options_dices_temp


def dice_num_generator(choice, dices):
    if len(choice) == dices:
        return 6
    else:
        return dices-len(choice)


def score_from_dice_num(dice_num, score, levels, wants_choice):
    if(dice_num == 6):
        return value
    possible_scores = list()
    for i in combinations_generator(dice_num):
        temp_score = best_choice(i, score, levels, 0)
        possible_scores.append(temp_score)
    average_score = sum(possible_scores) / len(possible_scores)
    if average_score < 0:
        return_score = 0
    else:
        return_score = average_score
    if wants_choice == 1:
        if return_score > 0:
            return "Roll the dice"
        else:
            return "Bank the points"
    else:
        return return_score

def score_from_dice_num_start(dice_num, score, levels, wants_choice):
    possible_scores = list()
    for i in combinations_generator(dice_num):
        temp_score = best_choice(i, score, levels, 0)
        possible_scores.append(temp_score)
    average_score = sum(possible_scores) / len(possible_scores)
    if average_score < 0:
        return_score = 0
    else:
        return_score = average_score
    if wants_choice == 1:
        if return_score > 0:
            return "Roll the dice"
        else:
            return "Bank the points"
    else:
        return return_score


def combinations_generator(dice_num):
    return_combinations = list()
    for roll in product([1, 2, 3, 4, 5, 6], repeat=dice_num):
        return_combinations.append(roll)
    return return_combinations


options_dices = {
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


t = 0
while options_generator() != options_dices:
    options_dices = options_generator()
    t += 1
    #print("t",t)

#print(options_dices)

# dice_combinations = dict()
#
#
# for d6 in range(1,7):
#     for d5 in range(1,7):
#         for d4 in range(1, 7):
#             for d3 in range(1, 7):
#                 for d2 in range(1, 7):
#                     for d1 in range(1, 7):
#                         current_dices = [d1, d2, d3, d4, d5, d6]
#                         current_dices.sort()
#                         current_dices_tuple = tuple(current_dices)
#                         if current_dices_tuple in dice_combinations:
#                             dice_combinations[current_dices_tuple] += 1
#                         else:
#                             dice_combinations[current_dices_tuple] = 1
# print(dice_combinations)
# choices = dict()
#
# for i in dice_combinations.keys():
#     choices[i] = list()
#     for j in options_dices.keys():
#         if not Counter(j) - Counter(i):
#             choices[i].append(j)
#
# print(choices[(2, 2, 3, 3, 4, 6)])

# print(options_dices)
# print(t)
# print(best_choice((1, 2, 4, 5, 5, 5), 0, 2, 1))
# a = (score_from_dice_num(1, 0, 1, 0))
# b = (score_from_dice_num(2, 0, 1, 0))
# c = (score_from_dice_num(3, 0, 1, 0))
# d = (score_from_dice_num(4, 0, 1, 0))
# e = (score_from_dice_num(5, 0, 1, 0))
f = (score_from_dice_num_start(6, 0, 100, 0))

print(f)
