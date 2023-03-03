def printMemberInfo(name, email, major, grade):
    print('name \t:', name)
    print('email \t:', email)
    print('major \t:', major)
    print('grade \t:', grade)
    print('--------------------------------')

# 매개변수 키워드 사용하지 않음
printMemberInfo('Mr. kim', 'kim@gmail.com', 'art', 1)

# 매개변수 키워드 사용함
printMemberInfo(grade=4, major='computer', email='abc@gmail.com', name='Mr. hong')
printMemberInfo(major='sport', grade=2, name='Mr. cong', email='def@gmail.com')
printMemberInfo(email='ghi@gmail.com', major='music', name='Mr. wang', grade=1)
