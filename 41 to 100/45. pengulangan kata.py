#pengulangan kata 
#dibuat pada 13/12/2024
# oleh dzaky fadhilah rahmawan
inputan_jumlah = int(input("masukan jumlah perulangan = "))
inputan_kalimat = str(input("masukan kalimat yang ingin diulang = "))
for i in range(inputan_jumlah):
    print(f"{i + 1}.{inputan_kalimat}.")