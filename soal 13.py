x = int(input("Masukkan bilangan bulat pertama (x): "))
y = int(input("Masukkan bilangan bulat kedua (y): "))
z = int(input("Masukkan bilangan bulat ketiga (z): "))

if x >= y and x >= z:
    terbesar = x
elif y >= x and y >= z:
    terbesar = y
else:
    terbesar = z

if x <= y and x <= z:
    terkecil = x
elif y <= x and y <= z:
    terkecil = y
else:
    terkecil = z

print("Nilai terbesar adalah:", terbesar)
print("Nilai terkecil adalah:", terkecil)
