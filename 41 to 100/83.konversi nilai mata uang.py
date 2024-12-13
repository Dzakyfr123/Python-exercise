# konversi nilai mata uang
#di buat pada 13/12/2024
#dzaky fadhilah rahmawan

def konversi_mata_uang(jumlah_rupiah, mata_uang_tujuan):

  kurs = {
    "USD": 15000,
    "EUR": 16500,
    "SGD": 11000
  }

  if mata_uang_tujuan in kurs:
    hasil_konversi = jumlah_rupiah / kurs[mata_uang_tujuan]
    return f"{jumlah_rupiah} Rupiah setara dengan {hasil_konversi:.2f} {mata_uang_tujuan}"
  else:
    return "Maaf, mata uang tujuan tidak tersedia."


jumlah = float(input("Masukkan jumlah uang dalam Rupiah: "))
tujuan = input("Masukkan kode mata uang tujuan (USD, EUR, SGD): ").upper()

hasil = konversi_mata_uang(jumlah, tujuan)
print(hasil)