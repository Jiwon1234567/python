from glob import glob
import random

def convertRsp(rsp):
    if rsp == 0:
        print('가위')
    elif rsp == 1:
        print('바위')
    elif rsp == 2:
        print('보')

def setUNum(ns):
    global userNum
    userNum = ns
    
def getUNum():
    return userNum

def setCNum():
    global comNum
    comNum = random.randint(0, 2)

def getCNum():
    return comNum

def victory(com, user):
    if com == user:
        print('무승부!')
    elif com - user == 1 or com - user == -2:
        print('컴퓨터 승리!')
    else:
        print('User 승리!')