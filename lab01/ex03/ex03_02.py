def dnl(lst):
    return lst[::-1]
input_list=input("Nhap danh sach cac so, cach nhau bang dau phay: ")
numbers=list(map(int, input_list.split(',')))
ldn=dnl(numbers)
print("List dau khi dao nguoc:",ldn)