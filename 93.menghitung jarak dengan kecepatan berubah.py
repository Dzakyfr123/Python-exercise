#kalkulator BMI
#di buat pada 13/12/2024
#oleh dzaky fadhilah rahmawan

tinggi = float(input("Masukkan tinggi badan Anda dalam meter: "))
berat = float(input("Masukkan berat badan Anda dalam kilogram: "))

bmi = berat / (tinggi ** 2)

print("BMI Anda adalah:", bmi)

if bmi < 18.5:
    print("Anda kekurangan berat badan.")
elif 18.5 <= bmi < 25:
    print("Berat badan Anda ideal.")
elif 25 <= bmi < 30:
    print("Anda kelebihan berat badan.")
else:
    print("Anda obesitas.")