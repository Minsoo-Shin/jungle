# 입국심사를 기다리는 사람 수 n
# 한 명을 심사하는데 걸리는 시간 배열 times
# 출력) 모든 사람 심사를 받는데 걸리는 시간의 최소값


def solution(n, times):
    answer = 0
    left = 1 # 소요시간의 예상 최소값
    right = max(times) * n # 소요시간의 예상 최대값
    while left <= right:
        mid = (left + right) // 2 
        people = 0 
        # 소요시간(mid)안에 n명의 사람을 처리할 수 있는지 판단
        # 가능하다면 소요시간(mid) 타이트하게
        # 불가능하다면 소요시간(mid) 느슨하게
        for time in times: 
            people += mid//time
            if people >= n:
                break
        if people >= n:
            answer = mid
            right = mid-1
        elif people < n:
            left = mid + 1
    return answer

