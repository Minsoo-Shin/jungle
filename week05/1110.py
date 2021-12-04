n = str(input())
new = str(n)
cnt = 0
while True:
    if len(new) == 1:
        a, b = 0, int(new[0])
    else:
        a, b = int(new[0]), int(new[1])
    new = str(b) + str(a+b)[-1]
    cnt += 1
    if int(new) == int(n):
        print(cnt)
        break
