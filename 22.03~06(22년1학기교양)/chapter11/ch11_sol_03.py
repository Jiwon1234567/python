def calculator(num1, num2):
    result1 = num1 + num2
    result2 = num1 - num2
    result3 = num1 * num2
    result4 = num1 / num2
    
    return (result1, result2, result3, result4)

inputNumber1 = int(input('정수를 입력하세요. '))
inputNumber2 = int(input('정수를 입력하세요. '))

result = calculator(inputNumber1, inputNumber2)
print('사칙연산 결과 : ', result)
