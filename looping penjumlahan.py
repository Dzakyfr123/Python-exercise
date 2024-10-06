total = 0
n = int(input("Masukkan jumlah angka yang ingin dijumlahkan: "))

for i in range(n):
    angka = float(input(f"Masukkan angka ke-{i + 1}: "))
    total += angka

print(f"Total dari angka yang dimasukkan adalah: {total}")
