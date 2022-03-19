num = input()
length = len(num)
ans = 0
if num[:2] == '0x':
    for i in range(2, length): 
        digit = num[i]
        if digit.isalpha():
            digit = ord(num[i]) - 87 
        ans += int(digit) * (16 ** (length-i-1))
    print(ans)
elif num[0] == '0':
    for i in range(1, length):
        ans += int(num[i]) * (8 ** (length-i-1))
    print(ans)
else:
    print(int(num))


