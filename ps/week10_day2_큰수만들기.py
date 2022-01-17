def solution(number, k):
    stack = [number[0]]
    length = len(number)

    for i in range(1, length):
        if stack[-1] >= number[i]:
            stack.append(number[i])
        else:
            while len(stack) != 0 and stack[-1] < number[i] and len(stack) + (length - 1 - i) >= length - k:
                stack.pop()
            stack.append(number[i])
    
    return ''.join(stack[:length - k])

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
# 테스트 12번 예외 케이스
print(solution("54321", 3))