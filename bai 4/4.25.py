print('sinh vien: le cong manh tung')
print('mssv: 235752021610041' )
print('##########')
numbers = input("Nhập các số, phân tách bằng dấu phẩy: ").split(',')
odd_numbers = [int (num) for num in numbers if int (num) % 2 != 0]
print(",".join(map(str, odd_numbers)))
