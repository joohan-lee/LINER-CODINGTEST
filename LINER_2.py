def solution(inp_str):
    answer = []
    #rule1
    if not (len(inp_str) >= 8 and len(inp_str) <= 15):
        answer.append(1)
    
    r2, r3, r4, r5 = False, False, False, False
    kindList = [False, False, False, False] #2번 4개 만족 여부
    maxRepeat = 0
    dict = {}
    i = 0
    maxCount = 0
    for c in inp_str:
        #rule2
        if r2 == False and not (c.encode().isalnum() or c in "~!@#$%^&*"): #문자가 영어, 숫자이면 ok(1,2,3)
            r2 = True
            answer.append(2)
        
        #rule3
        if c.encode().isupper():
            kindList[0] = True
        elif c.encode().islower():
            kindList[1] = True
        elif c.isdigit():
            kindList[2] = True
        elif c in "~!@#$%^&*":
            kindList[3] = True
        
        #rule4
        if i > 0:
            if inp_str[i] == inp_str[i-1]:
                maxCount += 1
        else:
            maxCount = 1
        i += 1
        
        #rule5
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
        
        
        
    if kindList.count(True) < 3:
        answer.append(3)
    
    if maxCount >= 4:
        print("maxCount", maxCount)
        answer.append(4)
    
    for v in dict.values():
        if v >=5:
            answer.append(5)
            break
            
    
    #모두 만족하는 경우 0 return
    if len(answer) == 0:
        result = 0
    else:
        result = answer
    return result

print(solution("abccccbab~!a-aakkkk"))
