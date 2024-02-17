import itertools
N, result, hands = int(input()), [], [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 0]
for combination in itertools.combinations(hands, 2): 
    if sum(combination) == N: result.append(combination)
print(len(set(result)))