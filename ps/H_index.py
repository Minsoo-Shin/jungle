def solution(citations):
    citations.sort()
    index_max = 0
    for i in range(1, 1001):
        up = 0
        for citat in citations:
            if citat >= i:
                up += 1
        if up >= i:
            index_max = max(index_max, i)

    return index_max
print(solution([4, 4, 4, 4, 3]))