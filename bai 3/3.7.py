n=int (input ("nhập vào một số: ") )
def checkValue(n):
    if n % 2 == 0:
        print("Đây là một số chẵn")
    else:
        print("Đây là một số lẻ")
checkValue(n)