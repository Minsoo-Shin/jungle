# def solution(citations):
#     citations.sort()
#     index_max = 0
#     for i in range(1, 1001):
#         up = 0
#         for citat in citations:
#             if citat >= i:
#                 up += 1
#         if up >= i:
#             index_max = max(index_max, i)

#     return index_max
# print(solution([4, 4, 4, 4, 3]))

def solution(citations):
    citations.sort()
    h_index = 0
    s = 0
    e = len(citations)
    while s <= e:
        m = (s + e)//2
        if citations[m] >= len(citations) - m:
            e = m - 1
        else:
            s = m + 1
            h_index
        
# def solution(citations):
#     citations.sort(reverse=True)
#     print(citations)
#     for idx , citation in enumerate(citations):
#         if idx >= citation:
#             return idx
# print(solution([0, 1, 3, 5, 6]))

def solution(citations):
    citations.sort()
    n = len(citations)
    left = 0
    right = n - 1
    max_h = 0
    while left <= right :                   ## < 아닌 <= 해야 구현됨, 왜?
        mid = (left + right) // 2
        if citations[mid] >= n -  mid :
            max_h = n - mid
            right = mid - 1
        else :
            left = mid + 1

    return max_h