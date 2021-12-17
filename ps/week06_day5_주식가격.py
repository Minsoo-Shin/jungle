# 가격 리스트 [1,2,3,2,3]
# 반환값      [4,3,1,1,0]
# 주식이 떨어진 시점의 초

# 탐색시 마지막 원소에 다다르면 0을 반환하고 종료하는 예외 처리해줘야함
# 결국 For문으로 마지막을 지정하여 예외 처리 안함

'''
계산양 : (n-1) + (n-2) + (n-3) + --- + 3 + 2 + 1 = n^2/2
prices 길이는 최대 100,000이다. 10^10 정도의 처리가 필요하다. 
최악의 경우 O(n^2)의 시간 복잡도를 가지는데 왜 통과될까?
'''

# 테스트 성공 (내 풀이)
# 브루트 포스를 활용한 문제 풀이
def solution(prices):
    answer=[]
    for i in range(len(prices)):
        i_ans = 0
        for j in range(i+1, len(prices)):
            i_ans += 1
            if prices[i] > prices[j]: break
        answer.append(i_ans)
    return answer

print(solution([100,100,100,100,100]))

# 테스트 성공 (내 풀이)
# DP를 활용한 문제 풀이 
# 속도면에서 차이가 없음, 
def solution(prices):
    dp = [0] * len(prices)
    for i in range(len(prices)-1, -1, -1):
        i_ans = 0
        # 가격이 위라면 계속 for문 => 여기 떄문에 속도 차이가 없는건가?
        # 아래 for문을 돌다가 가격이 같다면 dp 활용
        # 가격이 아래라면 해당
        for j in range(i+1, len(prices)):
            i_ans += 1
            if prices[i] == prices[j]:
                i_ans = dp[j] + j-i
                break
            if prices[i] > prices[j]: break
        dp[i] = i_ans
    return dp

# print(solution([100,101,102,103,104]))

# 테스트 성공 (다른 사람 풀이)
# Stack을 활용한 풀이
# 속도 매우 우수
# def solution(prices):
#     length = len(prices)
#     answer = [ i for i in range (length - 1, -1, -1)]
    
#     stack = [0]
#     for i in range (1, length, 1):
#         while stack and prices[stack[-1]] > prices[i]:
#             j = stack.pop()
#             answer[j] = i - j
#         stack.append(i)
#     return answer