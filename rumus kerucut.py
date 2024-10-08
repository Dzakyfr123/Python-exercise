print('='*30)
 print ('rumus kerucut')
 print('='*30)

 siku = int(input('masukan siku-siku: '))
 jari =int(input('masukan jari-jari:'))
 tinggi =int (input('masukan tinggi: '))
 
 ls = lambda a,b : 3.14 * b * a
 lp = lambda a,b : (3.14 * b * a) + (31.4 *b*b)
 v = lambda b,c : 1/3 *3.14 *b*b *c

 print('hasil luas alas :',ls(siku,jari))
 print ('hasil luas pemukaan ;',lp(siku,jari))
 print ('hasli seluruh:',v(jari,tinggi))