from itertools import product
from functools import reduce

def unique_pass(line):
    nums = list(map(int, line[:10]))
    password = ''.join(line[10:])
    alpha_letters = ['A', 'B', 'C', 'D', 'E']
    letter_to_nums = {}
    for i in range(0, 10, 2):
        letter_to_nums[alpha_letters[i//2]] = [nums[i], nums[i+1]]
    nums_group = [letter_to_nums[letter] for letter in password]
    combinations = list(product(*nums_group))
    return combinations

num_test = 1
while True:
    n = int(input())
    if n == 0:
        break
    combinations = []
    for _ in range(n):
        line = list(input().split())
        combinations.append(unique_pass(line))
    sets = [set(comb) for comb in combinations]
    result = reduce(set.intersection, sets)
    print(f'Teste {num_test}')
    for r in list(result)[0]:
        print(r, end=' ')
    print('\n')
    num_test += 1
    