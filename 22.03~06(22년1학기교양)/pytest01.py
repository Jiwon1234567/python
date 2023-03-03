import module01 as rn

print('가위 바위 보를 선택하세요. ')
choose = int(input('0.가위, 1.바위, 2.보 '))

rn.setCNum()
rn.setUNum(choose)

print('Com : ', end='')
rn.convertRsp(rn.getCNum())

print('User : ', end='')
rn.convertRsp(rn.getUNum())

rn.victory(rn.getCNum(), choose)