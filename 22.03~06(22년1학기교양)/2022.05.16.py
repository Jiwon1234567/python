'''
sum = 0
average = 0.0

while True:
    print('*'*20)
    print('성적처리 프로그램')
    print('*'*20)
    print('1. 성적 입력')
    print('2. 성적 출력')
    print('3. 종료')
    print('-'*20)

    
    menu = int(input('메뉴를 선택하세요(1~3) : '))
    
    while True:
        if menu <= 3 and menu >= 1:
            break
        else:
            print('메뉴(1~3)를 확인하세요')
            menu = int(input('메뉴를 선택하세요(1~3) : '))

    if menu == 1:
        print()
        korean = int(input('국어 성적을 입력하세요 : '))
        while True:
            if korean >= 0 and korean <= 100:
                break
            else:
                print('성적 범위(0~100)를 확인하세요')
                korean = int(input('국어 성적을 입력하세요 : '))
        english = int(input('영어 성적을 입력하세요 : '))
        while True:
            if english >= 0 and english <= 100:
                break
            else:
                print('성적 범위(0~100)를 확인하세요')
                english = int(input('영어 성적을 입력하세요 : '))
        math = int(input('수학 성적을 입력하세요 : '))
        while True:
            if math >= 0 and math <= 100:
                break
            else:
                print('성적 범위(0~100)를 확인하세요')
                math = int(input('수학 성적을 입력하세요 : '))
        print()
        
        sum = korean + english + math
        average = sum / 3
    
    elif menu == 2:
        print()
        print('국어 : ', korean)
        print('영어 : ', english)
        print('수학 : ', math)
        print('총점 : ', sum)
        print('평균 : ', average)
        print()
    
    elif menu == 3:
        print('프로그램을 종료합니다.')
        break
'''
        
sum = 0
average = 0
subject = {'국어':0, '영어':0, '수학':0}

while True:
    print('*'*20)
    print('성적처리 프로그램')
    print('*'*20)
    print('1. 성적 입력')
    print('2. 성적 출력')
    print('3. 종료')
    print('-'*20)
    
    menu = int(input('메뉴를 선택하세요(1~3) : '))
    
    while True:
        if menu <= 3 and menu >= 1:
            break
        else:
            print('메뉴(1~3)를 확인하세요')
            menu = int(input('메뉴를 선택하세요(1~3) : '))

    if menu == 1:
        print()
        for i in subject.keys():
            subject[i] = int(input(str(i)+'성적을 입력하세요 : '))
        while True:
            if subject[i] >= 0 and subject[i] <= 100:
                break
            else:
                print('성적 범위(0~100)를 확인하세요')
                subject[i] = int(input(str(i)+'성적을 입력하세요 : '))
                
        '''
        subject['영어'] = int(input('영어 성적을 입력하세요 : '))
        while True:
            if subject['영어'] >= 0 and subject['영어'] <= 100:
                break
            else:
                print('성적 범위(0~100)를 확인하세요')
                subject['영어'] = int(input('영어 성적을 입력하세요 : '))
        subject['수학'] = int(input('수학 성적을 입력하세요 : '))
        while True:
            if subject['수학'] >= 0 and subject['수학'] <= 100:
                break
            else:
                print('성적 범위(0~100)를 확인하세요')
                subject['수학'] = int(input('수학 성적을 입력하세요 : '))
        print()
        '''
        
        for i in subject.keys():
            sum += subject[i]
        average = sum / 3
        
    
    elif menu == 2:
        print()
        print('국어 : ', subject['국어'])
        print('영어 : ', subject['영어'])
        print('수학 : ', subject['수학'])
        print('총점 : ', sum)
        print('평균 : ', average)
        print()
    
    elif menu == 3:
        print('프로그램을 종료합니다.')
        break
    
    