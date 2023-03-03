snack = {'새우깡': 0, '비비빅': 0, '초코파이': 0, '맛동산': 0}
snackPrice = {'새우깡': 1200, '비비빅': 400, '초코파이': 500, '맛동산': 1500}
sumPrice = 0

def printRecipt():
    print('='*30)
    for i in snack.keys():
        print(str(i), ' 구매 금액 \t: ', int(snack[i]) * int(snackPrice[i]), '원')
    print('='*30)
    print('총 구매 금액 \t\t:', sumPrice, '원')
    print('='*30)
    
for i in snack.keys():
    snack[i] = int(input(str(i)+ ' 구매 개수 : '))
    sumPrice += int(snack[i]) * int(snackPrice[i])
    
printRecipt()
