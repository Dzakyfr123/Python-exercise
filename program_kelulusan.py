#ini adalah program nilai kelulusan
#di buat 08/11/2024
#di buat oleh Dzaky Fadhilah rahmawan

nama = input('masukan nama anda : ')
nilaiuts  = int(input('masukan nilai uts anda :'))
nilaipas = int(input('masukan nilai pas anda :'))
nilaiharian = int(input('masukan nilai harian anda : '))

jumlah = nilaiharian + nilaipas + nilaiuts
rata = jumlah / 3

if rata >= 90 :
    print(f"{nama} = Nilai A")
elif rata <= 90 :
    print(f"{nama} = Nilai B")
elif rata <= 75 :
    print(f"{nama} = Nilai C")
else :
    print (f"{nama} = Nilai D")
