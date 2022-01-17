# 1. 차량이 out지점에서 몇 대가 존재하는지를 체크하고 남은 나머지 차량과 어떻게 구분하지?
# => stack에서 pop으로 하면 구분가능
# 2. 일단 차량이 한번씩은 카메라에 잡혀야하니 차량의 마지막지점까지 있는 모든 차량을 pop하면
# 최소를 보장한다. 

# cars = []
# 정렬하고
# for문 돌면서 
# 첫번째 원소의 마지막 지점을 등록하고 
# while을 돈다. 다음 첫번쨰 지점과 비교하면서 
# pop을 한다.
# 등록 될때 cnt += 1을 한다. 
from collections import deque
def solution(cars):
    answer = 0
    cars.sort(key = lambda x: x[1])
    cars = deque(cars)
    while cars:
        start, last = cars.popleft()
        answer += 1
        while cars and cars[0][0] <= last:
            cars.popleft()
    return answer


print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))