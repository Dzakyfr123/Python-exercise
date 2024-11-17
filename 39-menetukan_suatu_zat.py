# menenukan suatu zat
# di buat pada 17/11/2024
# di buat oleh Dzaky fadhilah rahmawan



print(30*"=")
print("PROGRAM MENENTUKAN ZAT".center(30))
print(30*"=")

inputan_suhu = int(input("masukan suhu = "))
if inputan_suhu <= 0:
    print("ini adalah zat padat")
elif 0 <= inputan_suhu < 100:
    print("ini adalah zat cair")
elif inputan_suhu > 100:
    print("ini adalah zat uap")