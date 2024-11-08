# program tahun kabisat
#di buat 08/11/2024
# di buat dzkay fahilah rahmawan
tahun = int(input("Masukkan tahun: "))

if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(f"{tahun} adalah tahun kabisat.")
else:
    print(f"{tahun} bukan tahun kabisat")