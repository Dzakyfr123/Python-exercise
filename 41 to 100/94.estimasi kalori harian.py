#estimasi kalori harian
# dibuat pada 13/12/2024
#oleh dzaky fadhilah rahmawan

umur = int(input("Masukkan usia Anda: "))
jenis_kelamin = input("Masukkan jenis kelamin Anda (Laki-laki/Perempuan): ")
tinggi = float(input("Masukkan tinggi badan Anda dalam cm: "))
berat = float(input("Masukkan berat badan Anda dalam kg: "))
tingkat_aktivitas = int(input("Tingkat aktivitas (1: Sedentary, 2: Lightly active, 3: Moderately active, 4: Very active): "))


if jenis_kelamin.lower() == "laki-laki":
    bmr = 66 + (13.7 * berat) + (5 * tinggi) - (6.8 * umur)
else:
    bmr = 655 + (9.6 * berat) + (1.8 * tinggi) - (4.7 * umur)


faktor_aktivitas = [1.2, 1.375, 1.55, 1.725, 1.9] 
kalori_harian = bmr * faktor_aktivitas[tingkat_aktivitas - 1]

print("Kebutuhan kalori harian Anda:", kalori_harian)