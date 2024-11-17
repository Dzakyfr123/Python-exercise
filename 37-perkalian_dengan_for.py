# perkalian menggunakan for
# di buat pada 17/11/2024
#di buat oleh Dzaky fadhilah rahmawan




print(30*"=")
print("PROGRAM TABEL PERKALIAN")
print(30*"=")

while True:
    try:
        input_user = int(input("masukan jumlah perkalian = "))
        print("*",end="\t")
        for i in range(1,input_user + 1):
            print(i, end="\t")
        print()

        for i in range(1,input_user + 1):
            print(i, end="\t")
            for j in range(1, input_user + 1):
                print(i * j,end="\t")
            print()
        while True:
            isdone = str(input("apakah masih mau lagi (y/t) ? =  "))
            if isdone == "y":
                break
            elif isdone == "t":
                exit()
            else:
                print("hanya masukan y atau t !")
                break
    except ValueError:
        print("inputan anda tidak valid")
        print("silahkan masukan angka bulat")
        break
print("TERIMA KASIH")