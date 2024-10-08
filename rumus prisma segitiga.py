 print('='*40)
 print('RUMUS UNTUK PRISMA SEGITIGA')
 print('='*40)

 isi = float(input('masukan jumlah panjang : '))
 q = float(input('masukan tinggi : '))
 w = float(input('masukan lebar : '))


 lp = lambda a,b,c: (a*3) * b + (1/2 *a * b * c)
 v = lambda a,b,c : (1/2 *a * b * c) * b

 print('hasil nya adalah volume:',v(isi,q,w),)
 print ('hasil luas permukaan:',lp(isi,q,w),)