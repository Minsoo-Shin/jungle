import math
def solution(brown, yellow):
    # yellow의 약수의 집합을 뽑고, 
    # 더한 값 + 4를 했을때 갈색 수와 같다면, 답이다. 
    # 가로길이는 세로길이보다 길거나 같다.
    answer = []
    for i in range(1, int(math.sqrt(yellow)) + 1):
        if yellow % i == 0:
            a = yellow // i
            if 2*(a+i) + 4 == brown:
                answer.extend([a+2, i+2])

    return answer


print(solution(10, 2))