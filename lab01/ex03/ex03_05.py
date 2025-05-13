def dslxh(lst):
    count_dict={}
    for item in lst:
        if item in count_dict:
            count_dict[item]+=1
        else:
            count_dict[item]=1
    return count_dict
input_string=input("Nhap danh sasch cac tu, cach nhau bang dau cach: ")
word_list=input_string.split()
slxh=dslxh(word_list)
print("So lan xuat hien cua phan tu:",slxh)
        