s = input()
 
def is_check(s):    # 올바른 괄호열인지 확인하는 함수
    stack = []
    flag = True
 
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
 
        else:    # ) ]
            if s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    flag = False
 
            else:    # ]
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    flag = False
 
    if not stack and flag:
        return True
    return False
 
def calc_value(s):    # 괄호의 값을 계산하는 함수
    stack = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
 
        else:    # ) ]
            if s[i] == ')':
                if stack[-1] == '(':
                    stack[-1] = 2
                else:    # 올바른 괄호열이기 때문에 숫자만 있다.
                    temp = 0
                    for idx in range(len(stack)-1, -1, -1):    # 괄호 만날 때까지 계속 더해주기 (XY) = X + Y
                        if stack[idx] == '(':    
                            stack[-1] = temp * 2
                            break
                        else:    # ==> type(stack[idx]) == int
                            temp += stack[-1]
                            stack.pop()
 
            else:    # ]
                if stack[-1] == '[':
                    stack[-1] = 3
                else:    # 올바른 괄호열이기 때문에 숫자만 있다.
                    temp = 0
                    for idx in range(len(stack)-1, -1, -1):    # 괄호 만날 때까지 계속 더해주기 (XY) = X + Y
                        if stack[idx] == '[':     
                            stack[-1] = temp * 3
                            break
                        else:    # ==> type(stack[idx]) == int
                            temp += stack[-1]
                            stack.pop()
    return sum(stack)
 
if is_check(s):
    print(calc_value(s))
else:
    print(0)