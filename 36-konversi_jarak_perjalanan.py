# konversi jarak perjalanan
# 17/11/2024
# di buat oleh Dzaky fadhilah rahmawan




print(30*"=")
print("PROGRAM KONVERSI JARAK PERJALANAN")
print(30*"=")

input_user = int(input("masukan jarak perjalanan (cm) = "))
KM = 100000
M = 1000
CM = 1

hasil_km = (int(input_user / KM ))
input_user = (int(input_user % KM))
hasil_m = (int(input_user / M))
input_user = (int(input_user % M))
hasil_cm = (int(input_user / CM))
input_user = (int(input_user % CM))

print(f"hasil konversi \nkilometer = {hasil_km:.2f}\nmeter = {hasil_m:.2f}\ncenti meter = {hasil_cm:.2f}")