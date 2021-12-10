from itertools import permutations

a = "088"

permu1 = set(permutations(a, 2))
permu2 = list(permutations(a, 2))

# do_join1 = "".join(permu1)
# do_join2 = "".join(permu2)

print(permu1)
print(permu2)

do_join1 = [int("".join(_)) for _ in permu1]
do_join2 = [int("".join(_)) for _ in permu2]

print(do_join1)
print(do_join2)

do_all1 = [[int("".join(_)) for _ in set(permutations(a, i))] for i in range(1,len(a)+1)]
do_all2 = [[int("".join(_)) for _ in set(permutations(a, i))] for i in range(1, len(a)+1)]

print(do_all1)
print(do_all2)
