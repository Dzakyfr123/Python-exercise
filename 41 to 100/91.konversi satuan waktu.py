#konversi satuan waktu
#di buat pada 13/12/2024
#oleh dzaky fadhilah rahmawan

jarak = float(input("Masukkan jarak tempuh (km): "))
kecepatan = float(input("Masukkan kecepatan (km/jam): "))

waktu_menit = (jarak / kecepatan) * 60

print("Waktu tempuh:", waktu_menit, "menit")