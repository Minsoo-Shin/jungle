from itertools import combinations_with_replacement
from collections import Counter

for elem in combinations_with_replacement(range(4), 2):
    cnt = Counter(elem)
    print(cnt[0])