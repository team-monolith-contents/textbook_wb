def gugu():
    n = int(input("원하는 구구단 숫자 입력>"))
    if n <1 or n>9:
        print("숫자를 잘못 입력하였습니다. 1~9 사이의 숫자를 입력하세요")
        return
    else :
        print(n,"단을 출력합니다.")

        for j in range(1,10):
            print(n,"x",j,"=",n*j)
