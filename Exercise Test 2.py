def CheckNumberic(Check):
    while True:
        Note = input(Check)
        try:
            return int(Note)
        except ValueError:
            print("Fck u enter a number dumbass.")


def ADEQUY (Value):
    if Value <= 0:
        return 0

    return Value + ADEQUY(Value - 1)

def CheckPrime (Value):
    if Value == 2:
        return True
    if Value == 3:
        return True
    if Value % 2 == 0:
        return False
    if Value % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= Value:
        if Value % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def OutputMultiTable(Value):
    for x in range(1,Value + 1):
        print(*("{:3}".format(x*y) for y in range(1,Value+1)))

def LietKeNTNho(Value,list):
    for i in range(1,Value):
        if CheckPrime(i) == True:
            list.append(i)
    return list

if __name__ == '__main__':
    Value = CheckNumberic("Nhap vao mot so :")
    S = ADEQUY(Value)
    print ("Ket qua cua S(n) = ",S)
    Value2 = CheckNumberic("Nhap vao mot so de kiem tra so co phai la so nguyen to: ")
    P = CheckPrime(Value2)
    if P == True:
        print("%d la so nguyen to" % Value2)
    else:
        print("%d khong la so nguyen to" % Value2)
    Value3 = CheckNumberic("Ban muon in ra bang cuu chuong  tu 1 den bao nhieu: ")
    OutputMultiTable(Value3)
    list=[]
    Value4 = CheckNumberic("Nhap mot so de in ra cac so Nguyen To nho hon :")
    LIST = LietKeNTNho(Value4,list)
    print ("cac So Nguyen To Nho Hon So Vua nhap la: ",LIST)

