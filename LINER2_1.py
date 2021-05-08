def solution(program, flag_rules, commands):
    answer = []

    dictFlag = {} #flag 별 인자 type 매칭
    
    for flag_rule in flag_rules:
        flagArr = flag_rule.split(' ')
        if not (flagArr[0] in dictFlag):
            dictFlag[flagArr[0]] = flagArr[1] #KEY : VALUE 를 flag_name : flag_argument_type 으로 정의.
            
    
    
    for i in range(len(commands)):
        command = commands[i] #명령어 문자열
        

        cmdArr = command.split(' ') #명령어를 배열로
        cmdProgram = cmdArr[0]

        
        print("cmdProgram", cmdProgram)
        
        if not (cmdProgram == program): #조건 1 위배 시 다음 명령어 검사
            answer.append(False)
            continue

        dict_flag_count = {} #flag 별 횟수
        j = 1
        while j < len(cmdArr):
            flag_name = cmdArr[j]
            print("flag_name", flag_name)
            
            if flag_name in dictFlag: #flag_name이 유효(조건4)
                #조건 3. flag 중복 확인
                if flag_name in dict_flag_count:
                    answer.append(False)
                    break
                else:
                    dict_flag_count[flag_name] = 1
                

                #조건 2. 타입 확인
                if dictFlag[flag_name] == "STRING":
                    j += 1 #flag 인자 가져오기
                    
                    flag_argument = cmdArr[j]#flag 인자 가져오기
                    print("flag_argument", flag_argument)
                    if not (flag_argument.encode().isalpha()): #인자가 영어 대소문자가 아니면 False
                        answer.append(False)
                        break
                elif dictFlag[flag_name] == "NUMBER":
                    j += 1 #flag 인자 가져오기
                    
                    flag_argument = cmdArr[j]#flag 인자 가져오기
                    print("flag_argument", flag_argument)
                    if not (flag_argument.encode().isdigit()): #인자가 숫자인지 확인 후 아니면 False
                        answer.append(False)
                        break

                elif dictFlag[flag_name] == "NULL":
                    pass
                    #인자는 체크하지 않음

                else:
                    answer.append(False)
                    break
                    #유효하지 않은 flag 인자타입


            else:
               answer.append(False)
               break
                

                        
          


            j += 1

        if j == len(cmdArr): #조건을 모두 만족하면 True
            answer.append(True)
        
  

        
        

    
    
    
    return answer


print(solution("line",["-s STRING", "-n NUMBER", "-e NULL"],["line -n 100 -s hi -e", "lien -s Bye"]))

print(solution("line",["-s STRING", "-n NUMBER", "-e NULL"],["line -s 123 -n HI", "line fun"]))
print(solution("line",["-s STRING", "-n NUMBER", "-e NULL"],["line -s 123 -n HI", "line fun"]))

      
