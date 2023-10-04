aa=[]
for i in range(0,10,1):
    aa.append(0)
    id1= str(input("아이디를 입력하세요 : "))
    pass1=str(input("비밀번호를 입력하세요 : "))

    if id1 == "성결대학교" and pass1 == "파이데이아1":
        print("접속을 환영합니다")
    else:
        print("아이디와 비번을 정확히 입력하세요")

