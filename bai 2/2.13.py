print('sinh vien: le cong manh tung')
print('mssv: 235752021610041' )
print('##########')
import math

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: ") )
c = float(input("Nhập hệ số c: "))

if a == 0:

    if b == 0:
        print ("Phương tình vô nghiệm" if c != 0 else "Phương trình có vô số ngiệm")
    else:
        print (f"Phương trình có nghiệm duy nhất: x = {-c / b} ")
else: 
    delta = b ** 2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt (delta) ) / (2 * a)
        x2 = (-b - math.sqrt (delta) ) / (2 * a)
        print (f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2} ")
    elif delta == 0:
        print (f"Phương trình có nghiệm kép: x = {-b / (2 * a)}")
    else:
        print ("Phương trình vô nghiệm")

