print('='*40)
print('rumus tentang balok')
print('='*40)

p = float(input('masukan panjang'))
l = float(input('masukan lebar'))
t = float(input('masukan tinggi'))

v = p * l * t
luas_permukaan = (2*p*t) + (2*p*l) + (2*l*t)
keliling = 4 * (p +l+t)

print('volume = ',v
     ,'luas permukaan =',luas_permukaan
      , 'keliling = ',keliling)