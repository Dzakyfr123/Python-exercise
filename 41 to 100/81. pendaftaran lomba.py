# pendaftaran siswa
#di buat pada 13/12/2024
# oleh dzaky fadhilah rahmawan

peserta = []

def daftar_peserta(nama, umur):
  peserta.append({"nama": nama, "umur": umur})
  print(f"{nama} berhasil didaftarkan!")

daftar_peserta("Andi", 20)
daftar_peserta("Budi", 18)

print("\nDaftar Peserta:")
for peserta in peserta:
  print(f"Nama: {peserta['nama']}, Umur: {peserta['umur']}")