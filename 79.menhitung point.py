#menhitung point
# dibuat pada 13/12/2024
# oleh dzazky fadhilah rahmawan


uts = int(input("masukan nilai uts = "))
tugas = int(input("masukan nilai tugas = "))
uas = int(input("masukan nilai uas = "))
jumlah = uts + tugas + uas
rata_rata = jumlah / 3
# a > 85
# b 70 - 85
# c 60 - 70
print(f"rata rata nilai anda {rata_rata:.2f}")
if rata_rata >= 85:
    print(f"nilai anda A") 
elif 70 <= rata_rata < 85:
    print(f"nilai anda B")
elif 60 <= rata_rata < 70:
    print(f"nilai anda C")
elif rata_rata < 60:
    print(f"nilai anda D")