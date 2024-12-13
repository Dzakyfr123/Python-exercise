# konversi angka romawi
#dibuat pada 13/12/2024
# oleh dzaky fadhilah rahmawan

input = int(input("masukan angka integer = "))
if 1 <= input <= 9:
    print("inputan yang anda masukan benar")

angka_romawi = {
    1:"I",
    2:"II",
    3:"III",
    4:"IV",
    5:"V",
    6:"VI",
    7:"VII",
    8:"VIII",
    9:"IX",
    10:"X"
}
hasil_romawi = angka_romawi[input]
print(f"ini adalah angka romawinya {hasil_romawi}")