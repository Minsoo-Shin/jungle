str1 = list(" ") + list(input())
str2 = list(" ") + list(input())

d = [[0]*len(str2) for _ in range(len(str1))]
tracker = [[tuple() for _ in range(len(str2))] for _ in range(len(str1))]
for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            d[i][j] = d[i-1][j-1] + 1
            tracker[i][j] = (-1,-1)
        else:            
            if d[i-1][j] >= d[i][j-1]:
                d[i][j] = d[i-1][j]
                tracker[i][j] = (-1,0)
            else:
                d[i][j] = d[i][j-1]
                tracker[i][j] = (0,-1)

print(d[len(str1)-1][len(str2)-1])

result = str()
i = len(str1)-1
j = len(str2)-1 
while True:
    if i == 0 or j == 0: break
    if str1[i] == str2[j]:
        result += str1[i]    
    move_r, move_c = tracker[i][j]
    i += move_r
    j += move_c
    
result = result[::-1]
print(result)


        

