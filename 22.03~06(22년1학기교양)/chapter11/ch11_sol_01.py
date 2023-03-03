flag = True
totalVisitor = 0;

def countVisitor():
    global totalVisitor
    totalVisitor += 1

while flag:
    inputData = int(input('1.웹사이트 방문, 2.종료 '))

    if inputData == 1:
        countVisitor()
        print('누적 방문 횟수 : ', totalVisitor)
    else:
        flag = False
