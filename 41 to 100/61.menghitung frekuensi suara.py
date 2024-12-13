#menghitung frekuensi suara
#di buat pada 13/12/2024
# oleh dzaky fadhilah rahmawan

while True:
    try:
        getaran = float(input("berapa jumlah getaran benda = "))
        waktu = float(input("berapa lama waktu getaran (detik) = "))
        frekuensi = getaran / waktu
        print(f"frekuensi benda ini adalah = {frekuensi:.2f} hz")
        while True:
            isdone = str(input("apakah masih mau lagi (y/t) = "))
            if isdone == "y":
                break
            elif isdone == "t":
                exit()
                break
    except ValueError:
        print("inputan anda tidak valid ")
        print("silahkan masukan bilangan bertipe float saja")