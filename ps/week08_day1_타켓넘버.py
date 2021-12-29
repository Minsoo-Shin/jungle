def solution(numbers, target):
    stack = [[0,0]]
    ans = 0
    while stack:
        temp = stack.pop()
        for multiply in [-1,1]: 
            total, cnt = temp[0], temp[1]
            if cnt > len(numbers)-1: continue
            total += multiply * numbers[cnt]
            if cnt == len(numbers)-1 and total == target:
                ans += 1
            cnt += 1
            stack.append([total, cnt])
    return ans

print(solution([1, 1, 1, 1, 1], 3)) 