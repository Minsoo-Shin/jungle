import sys
input = sys.stdin.readline

n = int(input())
arr = [input().rstrip() for _ in range(n)]
arr = list(set(arr))
arr.sort(key=lambda x: (len(x), x))

for i in range(len(arr)):
    print(arr[i])

# import sys
# n = int(input())
# words = list(set(sys.stdin.readline().rstrip() for i in range(n)))

# words.sort(key=lambda x: (len(x), x))

# for word in words:
#     print(word)