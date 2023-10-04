print("메뉴판")
print("냉면 : 4000원")
print("짜장면 : 5000원")
print("짬뽕 : 6000원")
print("볶음밥 : 7000원")
print("탕수육 : 8000원")

money = int(input("가진돈 : "))

if money >=8000:
    print("시킬 수 있는 음식 : 냉면, 짜장면, 짬뽕, 볶음밥, 탕수육")
elif money <8000 and money>=7000:
    print("시킬 수 있는 음식 : 냉면, 짜장면, 짬뽕, 볶음밥")
elif money <7000 and money>=6000:
    print("시킬 수 있는 음식 : 냉면, 짜장면, 짬뽕")
elif money <6000 and money>=5000:
    print("시킬 수 있는 음식 : 냉면, 짜장면")
elif money <5000 and money>=4000:
    print("시킬 수 있는 음식 : 냉면")
else:
    print("시킬 수 있는 음식이 없습니다.")
    
    
            
