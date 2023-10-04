num1 = int(input("첫 번째 수를 입력하세요 : "))
num2 = int(input("두 번째 수를 입력하세요 : "))
num3 = int(input("세 번째 수를 입력하세요 : "))
num4 = int(input("네 번째 수를 입력하세요 : "))
num5 = int(input("다섯 번째 수를 입력하세요 : "))

count = 0

if num1/2 == num2:
    count = count + 1
elif num1/2 == num3:
    count = count + 1
elif num1/2 == num4:
    count = count + 1
elif num1/2 == num5:
    count = count + 1

elif num2/2 == num1:
    count = count + 1
elif num2/2 == num3:
    count = count + 1
elif num2/2 == num4:
    count = count + 1
elif num2/2 == num5:
    count = count + 1

elif num3/2 == num1:
    count = count + 1
elif num3/2 == num2:
    count = count + 1
elif num3/2 == num4:
    count = count + 1
elif num3/2 == num5:
    count = count + 1

elif num4/2 == num1:
    count = count + 1
elif num4/2 == num2:
    count = count + 1
elif num4/2 == num3:
    count = count + 1
elif num4/2 == num5:
    count = count + 1

elif num5/2 == num1:
    count = count + 1
elif num5/2 == num2:
    count = count + 1
elif num5/2 == num3:
    count = count + 1
elif num5/2 == num4:
    count = count + 1
else:
    count=0
    

print(count)
