def convertUnit(lenMm):

    unitDic = {}

    unitDic['cm'] = lenMm * 0.1
    unitDic['m'] = lenMm * 0.001
    unitDic['inch'] = lenMm * 0.03937
    unitDic['ft'] = lenMm * 0.003281

    return unitDic

def printLength(lengths):
    for len in lengths.keys():
        print(inputData, 'mm --> ', lengths[len], len)

inputData = int(input('길이(mm)를 입력하세요. '))

result = convertUnit(inputData)
printLength(result)
