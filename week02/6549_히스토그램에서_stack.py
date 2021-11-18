while True:
    temp = list(map(int, input().split()))
    n = temp[0]
    if n == 0:
        break
    heights = temp[1:]

    heights.insert(0, 0)
    heights.append(0)

    check = [0]
    area = 0

    for i in range(1, n+2):
        while check and heights[i] < heights[check[-1]]:
            cur_idx = check.pop()
            area = max(area, (i-1-check[-1])*heights[cur_idx])
        check.append(i)
    print(area)