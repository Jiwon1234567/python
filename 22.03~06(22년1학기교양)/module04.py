width = 32
length = 48

def sqareArea():
    square = 1
    global squareMax
    while square <= 32:
        if width % square == 0 and length % square == 0:
            squareMax = square
        square += 1

def printSquare():
    wid = width / squareMax
    len = length / squareMax
    print('정사각형 한 변의 길이 : ', squareMax, 'm')
    print('정사각형 한개 면적 : ', squareMax * squareMax, 'm^2')
    print('정사각형 개수 : ', wid * len)

