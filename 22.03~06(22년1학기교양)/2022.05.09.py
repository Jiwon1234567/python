korean = []

while 1:
    print('*'*20)
    print('성적처리 프로그램')
    print('*'*20)
    print('1. 성적 입력')
    print('2. 성적 출력')
    print('3. 종료')
    print('-'*20)
    
    menu = int(input('작업을 선택하세요(1 ~ 3) : '))
    
    if menu == 1:
        print('\n')
        for i in range(3):
            score = int(input('국어'+str(i+1)+' 성적을 입력 : '))
            korean.append(score)
        print('\n')
    elif menu == 2:
        sum = 0
        avg = 0.0
        print('\n')
        for item in korean:
            sum = sum + item
            print('국어', korean.index(item)+1, ' : ', korean[korean.index(item)])
        avg = sum / len(korean)
        print('총점 : ', sum)
        print('평균 : ', avg)
        print('\n')
    elif menu == 3:
        print('프로그램을 종료합니다.')
        break
        
        