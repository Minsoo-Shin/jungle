def solution(s):
    # 자르는 unit
    if len(s) == 1:
        return 1
    answer = float('inf')
    for unit in range(1, (len(s)//2)+1):
        temp_mul = 1
        prior = ''
        result = ''
        for i in range(0, len(s), unit):
            if s[i:i+unit] == prior:
                temp_mul += 1
            else:
                if temp_mul == 1:
                    result += prior
                else:
                    result += str(temp_mul) + prior
                prior = s[i:i+unit]
                temp_mul = 1
            if i >= len(s) - unit:
                if temp_mul == 1:
                    result += prior
                else:
                    result += str(temp_mul) + prior
        answer = min(answer, len(result))
        
    return answer