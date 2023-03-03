import random
from sre_parse import GLOBAL_FLAGS

word = ['Football', 'Pencil', 'Eraser', 'Car', 'Doll', 'Clock']
answer = ['축구', '연필', '지우개', '차', '인형', '시계']

def setUWord(uw):
    global userWord
    userWord = uw

def getUword():
    return userWord

def setCWord():
    global randNum
    global randWord
    global answerWord
    randNum = random.randint(0, 5)
    randWord = word[randNum]
    answerWord = answer[randNum]
    
def getComEngWord():
    return randWord

def getComKorWord():
    return answerWord

def correctWrong():
    global answerWord
    global userWord
    
    if userWord == answerWord:
        print('정답입니다.')
    else:
        print('틀렸습니다!!')
        print('한글 : ', answerWord)