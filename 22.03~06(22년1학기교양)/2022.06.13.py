def fun():
    print('module01의 함수가 실행됩니다.')
    
if __name__ == '__main__':
    fun()
    print('__name__', __name__)
    #변수값을 체크(모듈을 통해 실행되는건지, main함수 자체에서 실행되는건지 확인)
    #스스로 실행된거면 name에 main이 들어가고, 모듈을 통해 실행된거면 name에 파일명이 들어감
    