# menghitung panjang nama
#di buat pada 13/12/2024
#oleh dzaky fadhilah rahmawan
while True:
    try:
        input_nama = str(input("masukan nama anda = "))
        panjang_nama = len(input_nama)
        print(f"panjang nama anda adalah = {panjang_nama}")
        while True:
            isdone = str(input("apakah sudah beres ? (y/t) = "))
            if isdone == "y":
                break
            elif isdone == "t":
                print("TERIMA KASIH")
                exit()
            else:
                print("masukan y/t saja")
                break
    except ValueError:
        print("inputan anda tidak valid")
        print("masukan inputan bertipe string saja")