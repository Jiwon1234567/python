standardPrice = {'쌀':9900, '상추':1900,'고추':2900,'마늘':8900,'통닭':5600,'햄':6900, '치즈':3900}

def getDiscountPrice(rate):
    dcPrice = {}
    for goods in standardPrice.keys():
        disPri = int(standardPrice[goods] * (1 - (rate / 100)))
        dcPrice[goods] = disPri
    return dcPrice

def printPrice(priceList):
    for goods in priceList.keys():
        print(goods, '\t:', standardPrice[goods], '원\t', inputData, '%DC ->', priceList[goods], '원')

print('---------------------------------------------')
print('-- 한빛마트 오늘의 할인 가격표 출력 시스템 --')
print('---------------------------------------------')

inputData = int(input('오늘의 할인율을 입력하세요. '))
discountPrice = getDiscountPrice(inputData)

printPrice(discountPrice)
print('---------------------------------------------')
