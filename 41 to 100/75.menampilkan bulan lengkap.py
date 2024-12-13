#menampilkan bulan lengkap
#dibuat pada 13/12/2024
#oleh dzaky fadhilah rahmawan

import calendar

while True:
    try:
        tahun = int(input("masukan tahun (angka):"))
        bulan = int(input("masukan bulan (angka):"))
        print()
        print(f"hasil\n{calendar.month(tahun,bulan)}") 
        while True:
            isdone = str(input("apakah masih mau lagi (y/t) ? = "))
            if isdone == "y":
                break
            elif isdone == "t":
                print("TERIMA KASIH")
                exit()
            else:
                print("hanya masukan y / t !")
                break
    except ValueError:
        print("inputan anda tidak valid")
        print("silahkan masukan bilangan bulat")
        break
print("TERIMA KASIH")