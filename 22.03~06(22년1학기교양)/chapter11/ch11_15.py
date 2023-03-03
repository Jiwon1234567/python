import turtle
t = turtle.Turtle()
t.shape('turtle')

# 매개변수 값에 따라 도형을 그리는 함수
def drawShape(n):
    angle = 180 - (180 * (n - 2)) / n   # 터틀 회전각도
    
    for i in range(0, n):
        t.forward(100)
        t.left(angle)
    
num = int(input('원하는 도형을 입력하세요. ')) # 사용자가 원하는 도형 입력
drawShape(num)
