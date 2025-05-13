def tttl(lst):
    return tuple(lst)
input_list=input("Nhap danh sach cac so, cach nhau bang dau phay: ")
numbers = list(map(int, input_list.split(',')))
my_tuple=tttl(numbers)
print("List: ",numbers)
print("tuple tu List:",my_tuple)