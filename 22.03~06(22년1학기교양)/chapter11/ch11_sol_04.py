def fatorialFun(num):

    if num == 1:
        return 1
    else:
        return num * fatorialFun(num - 1)

inputData = int(input('0보다 큰 숫자를 입력하세요. '))
result = fatorialFun(inputData)
print( inputData, '팩토리얼은 ', result,'입니다.')
