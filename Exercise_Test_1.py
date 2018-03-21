def CheckNumberic(Check):
    while True:
        Note = input(Check)
        try:
            return int(Note)
        except ValueError:
            print("Fck u enter a number dumbass.")

def LietKeUocSo(list,N):
    for i in range(1,N+1):
        if N % i == 0:
            list.append(i)
    return (list)

def SumLietKe(list):
    Sum = int(0)
    print(list)
    for i in list:
        Sum = Sum + i
    return(Sum)

def FindMaxLe(list):
     MaxLe = int(0)
     for i in list:
         if i % 2 == 1 & i > 0:
             MaxLe = i
     return (MaxLe)

def CheckPerfectNum(N):
    Num = int(0)
    for i in range(1,N):
        if N % i == 0:
            Num += i
    if Num == N:
        return True
    return False

if __name__ == '__main__':
    list = []
    N = CheckNumberic("Nhap mot so: ")
    LIST=LietKeUocSo(list,N)
    #20
    print("Uoc so vua nhap: ",LIST,"\t")
    #print("Tong gia tri Uoc So Liet ke: %d" % sum(list))
    #21
    S = SumLietKe(list)
    print("Tong gia tri uoc so liet ke: ",S)
    #29
    M = FindMaxLe(list)
    print("So le lon nhat trong Uoc So la: ",M)
    #30
    PN = CheckPerfectNum(N)
    if PN == True:
        print ("Gia tri ",N, "vua nhap la so hoan thien")
    else :
        print("Gia tri ",N," vua nhap khong la so hoan thien")
