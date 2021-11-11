import random
heights = [int(input()) for i in range(9)]

while True:
    sampleList = random.sample(heights, 7)
    sampleList.sort()
    if sum(sampleList)==100:
        for sample in sampleList:
            print(sample)
        break