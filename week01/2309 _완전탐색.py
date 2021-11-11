from itertools import combinations
heights = [int(input()) for i in range(9)]

for array in list(combinations(heights, 7)):
    if sum(array) == 100:
        for i in sorted(array): print(i)
        break