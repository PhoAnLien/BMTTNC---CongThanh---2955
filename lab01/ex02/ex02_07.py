print("Nhap cac dong van ban(nhap 'done' de ket thuc):")
lines=[]
while True:
    line=input()
    if line.lower()=='done':
        break
    lines.append(line)
    print("\n Cac dong da duoc chuyen sang in hoa:")
    for line in lines:
        print(line.upper())