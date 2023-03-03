num = 10			# 전역변수 num 선언

def fun1():
    global num                    # 전역변수 num 설정
    num = 20		# 전역변수 num 변경
    print('num : ', num)	# 전역변수 num 사용

print('num : ', num)	# 전역변수 num 사용
fun1()
print('num : ', num)             # 전역변수 num 사용
