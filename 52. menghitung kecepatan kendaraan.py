#menghitung kecepatan kendaraan
#di buat pada 13/12/2024
# oleh dzaky fadhilah rahmawan

while True:
    try:
        jarak = int(input("masukan jarak berkendara (m) = "))
        waktu = int(input("masukan waktu berkendara (s) = "))
        kecepatan = jarak / waktu
        print(f"kecepatan kendaraan anda adalah = {kecepatan:.2f} m/s")
        while True:
            isdone = str(input("apakah mau lagi (y/t) ? = "))
            if isdone == "y":
                break
            elif isdone == "t":
                print("TERIMA KASIH")
                exit()
            else:
                print("silahkan masukan y/t saja ")
                break 
    except ValueError:
        print("inputan anda tidak valid")
        print("silahka masukan y/t saja")
print("TERIMA KASIH")