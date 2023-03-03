exam = {'국어':0,'영어':0,'수학':0}

def displayMenu():
    print()
    print('*'*20)
    print('성적처리 프로그램')
    print('*'*20)
    print('1. 성적 입력')
    print('2. 성적 출력')
    print('3. 종료')
    print('-'*20)
    
def inputScore():
    print()
    for i in exam.keys():
        while(True):
            score = int(input(i +' 성적을 입력하세요 : '))
            if score < 0 or 100 < score:
                print('성적(0~100) 범위를 확인하세요')
            else:
                break
        exam[i]= score
    
def printSumAvg():
    print()
    sum = 0
    avg = 0.0
    for i in exam.keys():
        sum += exam[i]
        print(i, ' 성적 : ', exam[i])
    avg = sum/len(exam)
    print('총점 : ',sum)
    print('평균 : ',avg)

while(True):
    displayMenu()
    
    while(True):
        menu = int(input('메뉴를 선택하세요(1 ~ 3) : '))
        if menu >= 1 or 3 <= menu:
            break
    
    if menu == 1:
        inputScore()
        
    elif menu == 2:
        printSumAvg()
        
    elif menu == 3:
        print('프로그램을 종료합니다.')
        break