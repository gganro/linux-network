XS,S,M,L,XL,XXL=0,0,0,0,0,0

aa=[]
for i in range(0,10,1):
    aa.append(0)
    
    size = int(input("치수를 입력하세요 : "))

    if size<=85:
        print("XS 입니다")
        XS = XS +1
    elif 85<size<=90:
        print("S 입니다")
        S = S+1
    elif 90<size<=95:
        print("M 입니다")
        M = M+1
    elif 95<size<=100:
        print("L 입니다")
        L = L+1
    elif 100<size<=105:
        print("XL 입니다")
        XL = XL+1
    elif 105<size<1000:
        print("XXL 입니다")
        XXL = XXL+1
    else:
        print("a")
    
print(XS,S,M,L,XL,XXL)

    
