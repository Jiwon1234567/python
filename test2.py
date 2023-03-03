def function_number1(count):
    i = 0
    sum = 0
    count2 = 0
    while i < count:
        i += 1
        num = int(input("n 횟수 입력"))
        if num % 2 == 0:
            sum += num
            count2 += 1
    return sum / count2

s = 0
m = int(input("m 정수 입력"))
s = function_number1(m)
print(s)