print ("="*40)
 print ("PROGRAM TABUNG")
 print ("="*40)

 r= float (input("masukan jari-jarinya"))
 t= float (input("masukan tinggi"))

 v = lambda a,b: 3.14 * a * a * b
 lp = lambda a,b : (2 * 3.14 * a * b) + ( 2 * (2 * 3.14 * a))
 
 print ("Volume :", v(r,t))
 print ("Luas permukaan:",lp(r,t))