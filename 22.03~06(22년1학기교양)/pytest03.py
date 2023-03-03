import module03 as mp3

if __name__ == '__main__':
    flag = True

while flag:
    playMenu = int(input('1.일반 재생 모드, 2.셔플 재생 모드 '))
    SongMenu = int(input('1.곡 추가, 2.곡 제거 '))

    mp3.selectSongMenu(SongMenu)
        
    mp3.selectPlayMenu(playMenu)

