def ttsc(lst):
    tong=0
    for num in lst:
        if num % 2 ==0:
            tong += num
            return tong
input_list =input("nhap danh sach so, cach nhau bang dau phay: ")
numbers = list(map(int, input_list.split(',')))
tongchan=ttsc(numbers)
print("Tong so chan trong List la:",tongchan)