num = 10                         # 전역변수 num 선언

def fun1():
    num = 20	           # 지역변수 num 선언
    print('num : ', num)       # 지역변수 num 사용(함수 안에서 num을 먼저 찾는다.)

print('num : ', num)           # 전역변수 num 사용
fun1()
