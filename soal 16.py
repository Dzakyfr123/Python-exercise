print('='*30)
print ('rumus kerucut')
print('='*30)





s = int(input('masukan siku-siku: '))
r =int(input('masukan jari-jari:'))
t =int (input('masukan tinggi: '))
 
ls = 3.14 * r * s
lp = (3.14 * r * s) + (31.4 *r*r)
hasil = 1/3 *3.14 *r*r *t

print('hasil luas alas :',ls)
print ('hasil luas pemukaan ;',lp)
print ('hasli seluruh:',hasil)