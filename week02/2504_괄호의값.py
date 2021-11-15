input_str = input()
ans = 0

def search_string(input_str):
    stack = [] #())
    for i in input_str: # 모든 string을 탐색하면서
        if i == '(' or i == '[': #해당 문자가 들어오면 stack에 저장한다. 
            stack.append(i)

        elif i == ')':
            ssum = 0
            while True:
                if not stack: return 0 
                temp = stack.pop()
                if temp == '(':
                    if ssum == 0:
                        ssum = 1
                    stack.append(2*ssum)
                    break
                elif temp == '[':
                    return 0
                else: # 나온게 숫자면 ssum에다가 저장하라.
                    ssum += temp
                    
        elif i == ']': 
            ssum = 0
            while True:
                if not stack:
                    return 0 
                temp = stack.pop()
                if temp == '[':
                    if ssum == 0:
                        ssum = 1
                    stack.append(3*ssum)
                    break
                elif temp == '(':
                    return 0
                else: # 나온게 숫자면 ssum에다가 저장하라.
                    ssum += temp
        elif not stack:
                return 0 
    return sum(stack)

print(search_string(input_str))