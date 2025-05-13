sogiolam=float(input("nhap so gio lam hang tuan: "))
luonggio=float(input("nhap thu lao tieu chuan moi gio: "))
giotieuchuan=44
giovuotchuan=max(0,sogiolam-giotieuchuan)
thuclinh=giotieuchuan*luonggio+giovuotchuan*luonggio*1.5
print(f"so tien thuc linh: {thuclinh}")