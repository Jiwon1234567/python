import turtle
t = turtle.Turtle()
t.shape('turtle')

# 매개변수 값에 따라 도형을 그리는 함수
def drawShape(x, y):
        
    t.up()
    t.goto(x, y)
    t.down()
    
    num = int(input('원하는 도형을 입력하세요. ')) 
    angle = 180 - (180 * (num - 2)) / num   # 터틀 회전각도
    
    for i in range(0, num):
        t.forward(100)
        t.left(angle)

s = turtle.Screen()

print("도화지에서 원하는 좌표를 클릭하세요.")
s.onscreenclick(drawShape)
