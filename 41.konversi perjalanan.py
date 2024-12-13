# konversi dalam perjalanan
# di buat pada 13/12/2024
# di buat oleh dzaky fadhilah rahmawan
input_cm = int(input("masukan jarak menggunakan cm = "))
KM = 100 * 10 * 100
M = 10 * 10
CM = 1


input_km = int(input_cm / KM)
input_cm = input_cm % KM
input_m = int(input_cm / M)
input_cm= input_cm % M
input_cm_1 = (input_cm / CM)
input_cm = input_cm % CM