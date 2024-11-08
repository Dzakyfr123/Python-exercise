# program tentang diskon
 # dibuat pada 08/11/2024
# di buat oleh Dzaky fadhilah rahmawan

barang1 = int(input('masukan harga barang pertama : '))
barang2 = int(input('masukan harga barang kedua : '))
barang3 = int(input('masukan harga barang ketiga : '))

jumlah = barang1 + barang2 + barang3
diskon = jumlah * 10 / 100
if jumlah >= 200000 :
    print('Selamat anda mendapatkan diskon dan sekarang menjadi ',diskon,)
else :
    print('silakan bayar dengan nominal ',jumlah)

    
