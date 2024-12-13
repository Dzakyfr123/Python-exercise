# menghitung jarak dengan kecepatan konstanta
#di buat pada 13/12/2024
#ole dzaky fadhilah rahmawan

kecepatan_awal = float(input("Masukkan kecepatan awal (m/s): "))
percepatan = float(input("Masukkan percepatan (m/s^2): "))
waktu = float(input("Masukkan waktu tempuh (s): "))

jarak = kecepatan_awal * waktu + 0.5 * percepatan * waktu**2

print("Jarak tempuh:", jarak, "meter")