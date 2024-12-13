#datadiri
#di buat pada 13/12/2024
#oleh dzaky fadhilah rahmawan

nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: "))
hobi = input("Masukkan hobi Anda (pisahkan dengan koma): ").split(",")

data_diri = {
    "nama": nama,
    "umur": umur,
    "hobi": hobi
}

print(data_diri)