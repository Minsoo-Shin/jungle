def solution(places):
    answer = []
    # 이중 포문을 돌면서 P의 좌표를 리스트에 담는다. 
    result = []
    for test in places:
        pos = []
        for i in range(5):
            for j in range(5):
                if test[i][j] == "P":
                    pos.append([i, j])
        # P의 좌표만 돌면서 맨해튼 거리 2초과하면 삭제한다. 
        needCheck = []
        for i in range(len(pos)):
            for j in range(i+1, len(pos)):
                if abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1]) <= 2:
                    needCheck.append([ [pos[i][0] , pos[i][1]], [pos[j][0] , pos[j][1]] ])
                    # [[1,3], [1,4]], [[1,3], [1,4]]....
        fail = False
        for check in needCheck:
            first, second = check[0], check[1]
            
            # # 남은 P만 가지고 사이에 거리두기를 준수했는지 체크하고 모두 지켜지고 있다면 1 아니면 0
            #세로인지 가로인지 대각선인지
            if abs(first[0] - second[0]) == 1 and abs(first[1] - second[1]) == 1:
                print(first[0], second[1], first[1], second[0])
                if test[first[0]][second[1]] != 'X' or test[second[0]][first[1]] != 'X':
                    result.append(0)
                    fail = True
                    break
            elif first[1] == second[1]:
                c = abs(first[0]+second[0])// 2
                if test[c][first[1]] != 'X':
                    result.append(0)
                    fail = True
                    break
            elif first[0] == second[0]:
                c = abs(first[1]+second[1])// 2
                if test[first[0]][c] != 'X':
                    result.append(0)
                    fail = True
                    break
                         
            # 한명이라도 거리두기를 안하면     
        if fail == False:
            result.append(1)
        answer = result 
        
    return answer