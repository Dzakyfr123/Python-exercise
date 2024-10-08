 print('='*40)
 print('rumus trapesium')
 print('='*40)


 alas1 = int(input('masukan alas pertama :'))
 alas2 = int(input('masukan alas kedua : '))
 tinggi = int(input('masukan tinggi : '))

 luas = lambda a,b,c : 1/2 *(a+b) * c

 print('luas trapesium tersebut adalah : ',luas(alas1,alas2,tinggi))
