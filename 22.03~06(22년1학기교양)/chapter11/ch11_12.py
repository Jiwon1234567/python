def divFunction(n1, n2):
    
    def divOperator(num1, num2):
        return num1 / num2
    
    if n2 != 0:
        result = divOperator(n1, n2)
    elif n2 == 0:
        result = '0으로 나눌 수 없습니다.'

    return result
    
print(divFunction(10, 0))
print(divFunction(10, 2))
