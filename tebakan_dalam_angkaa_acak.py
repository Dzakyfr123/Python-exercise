import random
angka_rahasia = random.randint (1, 100)
ditebak = None

while ditebak != angka_rahasia:
   ditebak=  int(input('masukan nomor acak dari 1 sampai 100 : '))
   if ditebak <= angka_rahasia :
      print('terlalu kecil')
   elif ditebak >= angka_rahasia :
      print('terlalu besar')
   else:
    print('selamat anda berhasil menebak nomor yang benar :',angka_rahasia)