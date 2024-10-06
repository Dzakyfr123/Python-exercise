harga_barang = float(input('masukan harga barang tersebut'))

if harga_barang > 100.000 :
    print ('anda mendapatkan diskon 5%')
else:
    print('banyakan belanja ubtuk mendapatkan diskon 5%')
diskon = 100 / 5
jumlah_pembayaran = harga_barang - diskon

print ('jumlah yang harus di bayar:',jumlah_pembayaran)