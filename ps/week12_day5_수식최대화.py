# 절대값 상 큰 값을 골라라
# 계산 우선순위는 랜덤하게 6가지 (+>->*, +>*>-, ->+>*, ->*>+, *>+>-, *>->+)
# 다 계산해보고 max_value을 갱신해라
# 그렇다면 문자열을 어떻게 계산할까?

from itertools import permutations

def solution(exp):
    max_v = -1
    cases = list(permutations('+-*'))
    
    stack = []
    while '+' in exp or '-' in exp or '*' in exp:
        for i in range(len(exp)):
            if exp[i] in '+-*':
                stack.extend([int(exp[:i]), exp[i]])
                exp = exp[i+1:]
                break
    stack.append(int(exp))

    
    for case in cases:
        temp = stack[:]
        for op in case:
            while op in temp:
                idx = temp.index(op)
                if op == '+':
                    temp = temp[:idx-1] + [temp[idx-1] + temp[idx+1]] + temp[idx+2:]
                elif op == '-':
                    temp = temp[:idx-1] + [temp[idx-1] - temp[idx+1]] + temp[idx+2:]
                else:
                    temp = temp[:idx-1] + [temp[idx-1] * temp[idx+1]] + temp[idx+2:]
        max_v = max(max_v, abs(temp[0]))
            
    return max_v

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
