# 통과 
# 다른사람 풀이

# 하드디스크 한번에 하나의 작업만
# 요청이 들어온 순서대로
# 누적합이 가장 작은

def solution(jobs):
    answer = 0
    time = 0
    n = len(jobs)
    jobs = sorted(jobs, key=lambda x: x[1])

    while jobs:
        for i in range(len(jobs)):
            if jobs[i][0] <= time:
                time += jobs[i][1]
                answer += time - jobs[i][0]
                jobs.pop(i)
                break
            
            if i == len(jobs) - 1:
                time += 1

    return answer // n