 panjang = int(input('masukan panjang\t :'))
 lebar = int(input('masukan lebar \t :'))
 luas = lambda p,l : p * l
 keliling = lambda p,l : 2 * (p +l)

 print('luas permukaan\t : ',luas(panjang,lebar),'cm2')
 print('keliling\t : ',keliling(panjang,lebar),'cm2')