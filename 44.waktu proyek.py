#waktu dalam proyek
#di buat pada 13/12/2024
#oleh dzaky fadhilah rahmawan
hari_input = float(input("masukan waktu pengerjaan proyek = "))
TAHUN = 365  
BULAN = 30
HARI = 1 

tahun = int(hari_input / TAHUN)
hari_input = hari_input % TAHUN
bulan = int(hari_input / BULAN )
hari_input = hari_input % BULAN
hari = int(hari_input / HARI)
hari_input = hari_input % HARI

print(f"waktu pengerjaan proyek ini adalah\n tahun = {tahun}\nbulan = {bulan}\nhari = {hari} ")