# def solution(land):
#     for i in range(1, len(land)):
#         for j in range(4):
#             if j == 0:
#                 land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
#             elif j == 1:
#                 land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
#             elif j == 2:
#                 land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
#             else:
#                 land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])
#     return max(land[len(land)-1])


def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j%4] += max(land[i-1][(j+1)%4],
                                land[i-1][(j+2)%4],
                                land[i-1][(j+3)%4])
    return max(land[len(land)-1])
    
print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
