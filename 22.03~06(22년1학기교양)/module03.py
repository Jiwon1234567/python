import random

song = ['Dynamite.mp3', '다시 여기 바닷가.mp3', '마리아 (Maria).mp3', 'When We Disco.mp3', 'How You Like That.mp3', '눈누난나.mp3', '그 여름을 틀어줘.mp3']

def selectSongMenu(sMenu):
    global addSong
    global delSong
    if sMenu == 1:
        addSong = input('추가할 곡을 입력하세요 : ')
        song.append(addSong)
        print('----- 곡 추가 :', addSong, '-----')
    elif sMenu == 2:
        delSong = input('제거할 곡을 입력하세요 : ')
        song.remove(delSong)
        print('----- 곡 제거 :', delSong, '-----')
        
def selectPlayMenu(pMenu):
    if pMenu == 1:
        print('----- 일반 재생 모드 -----')
        print('----- 곡 리스트 출력 -----')
        for i in range(0, len(song)):
            print(song[i])
    elif pMenu == 2:
        print('----- 셔플 재생 모드 -----')
        random.shuffle(song)
        print('----- 곡 리스트 출력 -----')
        for i in range(0, len(song)):
            print(song[i])