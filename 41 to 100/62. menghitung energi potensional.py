#menghitung energi potensional
# di buat pada 13/12/2024
# oleh dzaky fadhilah rahmawan

while True:
    try:
        massa = float(input("masukan massa sebuah benda (kg) = "))
        gravitasi = float(input("masukan besaran gravitasi (m/s) = "))
        ketinggian = float(input("masukan tinggi ketinggian benda tersebut dari tanah (m) = "))
        energi_potensial = massa * gravitasi * ketinggian
        print(f"energi potensial benda ini adalah = {energi_potensial:.2f}")
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