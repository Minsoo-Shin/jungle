import math
def solution(n, k):
    def findPrime(num):
        cnt = 1
        if num == 0 or num == 1: return 0
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                cnt += 1
        if cnt == 1:
            return 1
        else:
            return 0

    answer=0
    k_number = ""
    while n != 0:
        a = n // k
        b = n % k
        k_number += str(b)
        n = a
    k_number = k_number[::-1].split("0")
    # print(k_number)
    for num in k_number:
        if num != "":
            answer += findPrime(int(num))

    return answer

print(solution(437674,	3))
print(solution(110011, 10))