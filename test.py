def funtion_number1 (num):
    if m % 2 == 0:
        s = s + m
        k = k + 1
        return s/k

n=int(input("정수입력"))
i=1
while i < n+1 :
    m = int(input("정수입력"))
    
print(funtion_number1 (m))