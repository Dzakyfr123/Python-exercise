print('='*40)
print('RUMUS UNTUK PRISMA SEGITIGA')
print('='*40)

isi = float(input('masukan jumlah panjang : '))
q = float(input('masukan tinggi : '))
w = float(input('masukan lebar : '))

la = 1/2 * isi * q * w 
lp = (isi + isi + isi) * q + la
v = la * q

print('hasil nya adalah volume:',v,)
print ('hasil luas permukaan:',lp,)
