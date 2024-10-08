print('='*40)
 print('rumus tentang balok')
 print('='*40)

 p = float(input('masukan panjang'))
 l = float(input('masukan lebar'))
 t = float(input('masukan tinggi'))

 v = lambda a,b,c: a * b * c
 lp = lambda a,b,c : 2*(a*c) + (a*b) + (2*b*c)
 k = lambda a,b,c : 4 * (a+b+c)

 print('volume = ',v(p,l,t)
     ,'luas permukaan =',lp(p,l,t)
      , 'keliling = ',k(p,l,t))