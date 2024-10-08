print ("="*40)
 print ("PROGRAM LINGKARAN ")
 print ("="*40)

 jari_jari = float(input("masukkan Jari-jari")) 

 luas = lambda j : 3.14 * j
 keliling  = lambda j : 3.14 * 2 * j
 print ("luas:", luas(jari_jari) ," cm2")
 print ("keliling:", keliling(jari_jari) , " cm")