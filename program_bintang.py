#program bintang
# di buat pada 08/11/2024
# di buat oleh Dzaky Fadhilah Rahmawan

angka = int(input('masukan angka : '))

for i in range(1,angka + 1):
 print(i*"*")
print('ini adalah segitiga terbalik')
for i in range(1,angka + 1):
 print((angka - i + 1)*"*")