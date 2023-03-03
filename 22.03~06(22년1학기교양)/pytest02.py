import module02 as rd

rd.setCWord()
print('영어 : ', end='')
print(rd.getComEngWord())

korWord = input(('한글을 입력하세요. '))
rd.setUWord(korWord)

rd.correctWrong()

