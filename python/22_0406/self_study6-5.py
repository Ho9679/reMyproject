hap = 0
num1, num2, num3 = 0,0,0

num1 = int(input("시작값을 입력하세요 : "))
num2 = int(input("끝값을 입력하세요 : "))
num3 = int(input("증가값을 입력하세요 : "))

while num1 < num2+1:
    hap = hap + num1
    num1 = num1 + num3

print("%d에서 %d까지 %d씩 증가시킨 값의 합계 : %d" %(num1, num2, num3, hap))