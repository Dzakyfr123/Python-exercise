# data penjualalan
#di buat pada 17/11/2024
# di buat oleh Dzaky fadhliah rahmawan





print(30*"=")
print("PROGRAM MENGHITUNG DATA PENJUALAN MOBIL")
print(30*"=")
print()

data_penjualan = []
def input_user(input_jumlah):
    
    for i in range(input_jumlah):
        data = int(input(f"masukan hasil penjualan ke {i+1} = "))
        data_penjualan.append(data)
while True:
    
        input_jumlah = int(input("berapa jumlah data penjualan ? = "))
        input_user(input_jumlah)
        total = 0
        penjualan_terbanyak = data_penjualan[0]
        penjualan_terrendah = data_penjualan[0]
        for i in data_penjualan:
            total += i
            if i > penjualan_terbanyak:
                penjualan_terbanyak = i
            if i < penjualan_terrendah:
                penjualan_terrendah = i

        print(f"total jumlah penjualan = {total}")
        print(f"penjualan terbanyak = {penjualan_terbanyak}")
        print(f"penjualan terrendah = {penjualan_terrendah}")
        print(f"rata-rata penjualan = {total / len(data_penjualan)}")