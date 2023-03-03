clothes = {'티셔츠': 20000, '바지': 25000, '반바지': 15000, '스커트': 18000, '모자': 10000}

def calculate(name, money):
    for i in clothes.keys():
        if i == name:
            return money - clothes[i]
    

product = str(input('구매 상품을 입력하세요. '))
payment = int(input('지불 금액을 입력하세요. '))

charge = calculate(product, payment)

print('거스름 돈 :', charge)
