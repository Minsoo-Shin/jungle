'''
1.아이디어
    각 숫자당 필요한 세트의 수를 리스트에 담고, 최대값으 구하면 된다,. 
    6과 9는 합쳐서 절반 (6+9 +1)//2 
2.시간복잡도 
    방번호 백만
3.자료구조
    lst[인덱스] = 갯수

'''
import sys
input = sys.stdin.readline

string = input().strip()
lst = []
for i in range(10):
    lst.append(string.count(str(i)))
temp = (lst[6] + lst[9] + 1)//2
del lst[6], lst[8]
lst.append(temp)
print(max(lst))
