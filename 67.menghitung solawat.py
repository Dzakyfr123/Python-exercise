#menghitung ssolawat
#di buat pada 13/12/2024
#oleh dzaky fadhillah rahmawan

while True:
    try:
        input_sholawat = str(input("anda ingin bersholawat per (minggu/bulan/tahun) = "))
        sholawat_perhari = int(input("anda ingin bersholawat berapa perhari = "))
        if input_sholawat == "minggu":
            hasil = sholawat_perhari * 7
            print(f"anda telah bersholawat kepada nabi sebanyak : \n {hasil:,} sholawat per{input_sholawat}")
        elif input_sholawat == "bulan":
            hasil = sholawat_perhari * 30
            print(f"anda telah bersholawat kepada nabi sebanyak : \n {hasil:,} sholawat per{input_sholawat}")
        elif input_sholawat == "tahun":
            hasil = sholawat_perhari * 365 
            print(f"anda telah bersholawat kepada nabi sebanyak : \n {hasil:,} sholawat per{input_sholawat}")
        else:
            print("masukan minggu,bulan,tahun saja !")
            break
        while True:
            isdone = str(input("apakah sudah beres ? (y/t) = "))
            if isdone == "t":
                break
            elif isdone == "y":
                print("TERIMA KASIH")
                exit()
            else:
                print("masukan y/t saja")
                break
    except ValueError:
        print("inputan anda tidak valid")