a, b, c = map(int, input().split())


def g(a: int,b: int, c: int):
    if b==1:
        return a % c
    temp = g(a, b//2, c)
    if b % 2 == 0:
        return temp * temp % c
    else:
        return temp * temp * (a % c) %c
 
print(g(a,b,c))