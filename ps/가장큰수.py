# '''
# lambda x가 sort 
# '''
# def solution(numbers):
#     answer = ''
#     # 각 숫자의 크기를 0000로 만들어 준다. '
#     temp = []
#     for num in numbers:
#         base = num
#         str_digit = len(str(base))
#         if str_digit < 4:
#             base *= (10 **(4 - str_digit))
#         temp.append([base, num])
#     temp.sort(key = lambda x: (-x[0], len(str(x[1]))))
    
#     for group in temp:
#         answer += str(group[1])
#     # 크기대로 정렬, 두번째기준으로 len 작은 기준대로 정렬
#     # 두 번째 원소 기준으로 join하면 된다.   
#     return answer

def solution(numbers):
    answer = ''
    # string list를 만들고, 숫자가 두 자리 숫자면 뒤에 10을 넣는다. 
    temp = []
    for num in numbers:
        base = list(map(int, list(str(num))))
        str_digit = len(base)
        for _ in range(4 - str_digit):
            base.append(base[-1])
        temp.append((base, str(num)))
    # 리스트로 정렬을 해주고 
    temp.sort(key = lambda x: len(x[1]))
    temp.sort(key = lambda x: x[0], reverse = True)
    
    # x[1]로 붙이면 된다. 
    for int_num in temp:
        answer += int_num[1]
    answer = str(int(answer))

    return answer

print(solution([332, 33, 337]))


# def solution(num): 
#     num = list(map(str, num))
#     num.sort(key = lambda x : x*3, reverse = True) 
#     return str(int(''.join(num)))

if __name__ == "__main__":
    print(solution([3,30,34,5,9]))
