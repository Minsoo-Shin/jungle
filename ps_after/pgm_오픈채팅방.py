from collections import defaultdict
def solution(record):
    answer = []
    # 일단 Enter, Leave만 판단하여 리스트를 만든다. 
    nickInform = defaultdict(str)
    
    for rec in record:
        split_rec  = rec.split(" ")
        if split_rec[0] != "Leave":
            nickInform[split_rec[1]] = split_rec[2]
            
    for rec in record:
        if rec.split(" ")[0] == 'Enter':
            answer.append(nickInform[rec.split(" ")[1]] + "님이 들어왔습니다.")
        elif rec.split(" ")[0] == 'Leave':
            answer.append(nickInform[rec.split(" ")[1]] + "님이 나갔습니다.")
    
    return answer