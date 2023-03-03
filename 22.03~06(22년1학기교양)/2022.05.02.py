import random
randomNum = random.randrange(1, 101)
for i in range(1, 11, 1):
    i = int(input('1부터 100사이의 난수를 맞추세요. '))
    if i == randomNum:
        print('정답입니다.')
        break
    else:
        print('틀렸습니다. 다시 입력하세요.')
        if i < randomNum:
            print('난수는 입력한 숫자보다 작습니다.')
        else:
            print('난수는 입력한 숫자보다 큽니다.')
    range == 11
    print('게임에서 졌습니다.')
print('난수 : ', randomNum)