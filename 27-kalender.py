# program mmenentukan sebuah bulan
# di buat pada 17/11/2024
# di buat oleh dzaky fadhilah rahmawan

print(30 * "\033[92m=")
print("PROGRAM MENENTUKAN BULAN")
print(30 * "\033[92m=")

menu_bulan = {
    "januari": 1,
    "februari": 2,
    "maret": 3,
    "april": 4,
    "mei": 5,
    "juni": 6,
    "juli": 7,
    "agustus": 8,
    "september": 9,
    "oktober": 10,
    "november": 11,
    "desember": 12
}

for bulan, angka in menu_bulan.items():
    print(f"bulan = {bulan}, angka = {angka}")

# Input from user
input_user = int(input("Masukkan angka sesuai bulan = "))

# Find the month corresponding to the user input
for bulan, angka in menu_bulan.items():
    if angka == input_user:
        print(f"Angka yang Anda pilih adalah bulan = {bulan.capitalize()}")
        break
else:
    print("Input tidak valid! Masukkan angka antara 1 hingga 12.")
