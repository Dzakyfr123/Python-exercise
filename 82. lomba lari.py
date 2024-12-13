#lomba lari
#di buat 13/12/2024
#oleh dzaky fadhilah rahmawan

import random


peserta = ["Andi", "Budi", "Cici", "Dedi"]


def hitung_waktu():
  return random.uniform(10, 20)  


print("Perlombaan dimulai!")


hasil = {}
for peserta in peserta:
  waktu = hitung_waktu()
  hasil[peserta] = waktu
  print(f"{peserta} selesai dalam waktu {waktu:.2f} detik")


pemenang = min(hasil, key=hasil.get)
print(f"\nPemenangnya adalah {pemenang} dengan waktu {hasil[pemenang]:.2f} detik!")