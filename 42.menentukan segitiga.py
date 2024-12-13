#menentukan segtiga
#di buat pada 13/12/2024
# ole dzaky fadhilah rahmawan
a = float(input("masukan sisi a = "))
b = float(input("masukan sisi b = "))
c = float(input("masukan sisi terpanjang c = "))

if a**2 + b**2 == c**2:
    print("ini adalah segitiga siku siku")
elif a**2 + b**2 > c**2:
    print("ini adalah segitiga lancip")
elif a**2 + b**2 < c**2:
    print("ini adalah segitiga tumpul")
else:
    print('ini bukan segitiga')