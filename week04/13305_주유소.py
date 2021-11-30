# N개의 도시. 일직선 위에 놓여이음. 1km당 1L소진. 

# 최대한 저렴한데서 많이 넣는다. 
# 저렴한 곳에서 많이 넣기 위해 이동에 필요한 기름만 넣는다. 
n = int(input())
dist = list(map(int, input().split()))
oil = list(map(int, input().split()))

#마지막 도시의 오일은 무의미
i=0
ssum = 0
while i < n-1:
    if oil[i] <= oil[i+1]: # 다음 행선지의 오일가격이 비싸다면
        oil[i+1] = oil[i] #오일가격은 낮은걸로 한다. 
    ssum += oil[i] * dist[i] # 이번 행선지에서 쓸 거만 채운다.
    i += 1 

print(ssum)