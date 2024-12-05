print('sinh vien: le cong manh tung')
print('mssv: 235752021610041' )
print('##########')
dau_vao=input('nhập một câu: ')
chu_hoa=0
chu_thuong=0
for char in dau_vao:
    if char.isupper ():
        chu_hoa +=1
    elif char.islower ():
        chu_thuong +=1
print ('chữ hoa: ', chu_hoa)
print ('chữ thường: ', chu_thuong)
