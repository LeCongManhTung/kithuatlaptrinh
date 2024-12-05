print('sinh vien: le cong manh tung')
print('mssv: 235752021610041' )
print('##########')
j=[]
for i in range (2000, 3201):
    if (i%7 == 0) and (i%5 != 0):
        j.append(str(i))
print (', '.join (j))
