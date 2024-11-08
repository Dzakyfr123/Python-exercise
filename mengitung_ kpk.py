# program perhitungan kpk dan fgb
# di buat pada 08/11/2024
# di buat oleh Dzaky fadhilah rahmawan 


import math

angka1 = int(input('masukan angka pertama : '))
angka2 = int(input('masukan angka kedua : '))

fpb = math.gcd(angka1, angka2)
kpk = (angka2 , angka1)  // fpb

print(f"FPB dari {angka1} dan {angka2} = {fpb}")
print(f"KPK dari {angka1} dan {angka2} + {kpk}")
