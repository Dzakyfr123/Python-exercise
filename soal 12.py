Nama_siswa = input('Masukan nama siswa:')
nilai = float (input('masukan nilai anda: '))

if  90 <= nilai <= 100:
    print ('grade A')
elif 80 <= nilai <= 90:
    print ('grade B')
elif 70 <= nilai <= 80:
    print ('grade c')
elif 60 <= nilai <= 70:
    print ('grade D')
else:
    print('grade E')

print ('hasil dari nilai siswa dan siswi :',nilai)
