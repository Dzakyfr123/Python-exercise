print('='*40)
print('penggunaan if pada kodingan')
print('='*40)

nilai = int(input('masukan nilai anda'))

if 80 <= nilai <= 100 :

    print('sangat bagus')
elif 65 <= nilai <= 79:
    print ('bagus')
elif 40 <= nilai <= 64:
    print('kurang')
elif 1 <= nilai <= 39:
    print('perbaiki kembali')
else :
    print ('tidak terdaftar')