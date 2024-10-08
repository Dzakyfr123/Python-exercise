print('='*20)
 print('rumus bola')
 print('='*20)

 jari = int(input('masukan jari-jari tersebut\t :'))


 lp = lambda r : 4 * 3.14* (r*r)
 v = lambda r:(4/3)*3.14 *(r*r*r)
 k = lambda r :(4/3)*3.14*(r*r)

 print('luas permukaan\t:',lp(jari))
 print('volume\t:',v(jari))
 print('keliling\t:',k(jari))