# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

def solution(id):
    #1단계 
    id = id.lower() 
    
    #2단계
    new_id = ''
    for i in range(len(id)):
        if id[i].isalnum() or id[i] in ['-','_','.']:
            new_id += id[i]

    #3단계
    while ".." in new_id:
        new_id = '.'.join(new_id.split(".."))

    #4단계
    new_id = new_id.strip(".")

    #5단계
    if len(new_id) == 0:
        new_id += 'a'

    #6단계
    new_id = new_id[:15]
    new_id = new_id.rstrip(".")

    #7단계
    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id

# print(solution(	"...!@BaT#*..y.abcdefghijklm"))
# print(solution(	"z-+.^."))
# print(solution("=.="))
# print(solution("123_.def"))
# print(solution("abcdefghijklmn.p"))
# 반례
print(solution("aaaa"))


































# import string 

# def Del_str(text):
#     temp = ''
#     id_list = []
#     id_list.extend([i for i in string.ascii_lowercase])
#     id_list.extend([i for i in string.digits])
#     id_list.extend(['-','_','.'])
    
#     temp = ''
#     for i in text:
#         if i in id_list:
#             temp += i
#     return temp

# def empty_str(text):
#     if text == "":
#         return "a"
#     else:
#         return text

# def len_2_under(text):
#     while len(text) < 3:
#         text += text[-1]
#     return text

# def del_some_string(text):
#     while ".." in text:
#         text= text.replace("..", ".")
#     return text
    
# def solution(new_id):
#     answer = ''
#     new_id = new_id.lower()
#     new_id = Del_str(new_id)
#     new_id = del_some_string(new_id)
#     new_id = new_id.strip(".")
#     new_id = empty_str(new_id)
#     new_id = new_id[0:15].strip(".")
#     new_id = len_2_under(new_id)
#     answer = new_id
    
#     return answer