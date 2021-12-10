from functools import reduce 
a = [1,2,3,4,5]

print(reduce(lambda x, y: x+y, a))
print(list(filter(lambda x: x%2==0, a)))
