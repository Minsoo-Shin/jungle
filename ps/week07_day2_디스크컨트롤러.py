# 통과 
# 다른사람 풀이

def solution(jobs):
    answer = 0 
    time = 0
    n = len(jobs)
    # 소요시간이 적게 걸리는 작업부터
    jobs = sorted(jobs, key=lambda x: x[1])
    # 작업이 없을때까지 계속 진행
    while jobs:
        # 모든 작업에 대해서
        for i in range(len(jobs)):
            # time보다 낮은 작업이면서 적은 소요시간 작업 진행 
            if jobs[i][0] <= time:
                time += jobs[i][1]
                answer += time - jobs[i][0]
                jobs.pop(i)
                break
            # 마지막까지 확인했는데 없다면, time+=1 
            if i == len(jobs) - 1:
                time += 1

    return answer // n