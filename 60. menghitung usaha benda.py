#menghitung usaha benda
# di buat pada 13/12/2024
# oleh dzaky fadhilah rahmawan

while True:
    try:
        gaya = float(input("berapa besaran gaya benda (n) = "))
        perpindahan = float(input("berapa jauh perpindahan benda (m) = "))
        sudut = float(input("berapa besaran sudut benda (derajat) = "))
        usaha = gaya * perpindahan * sudut
        print(f"usaha benda ini adalah = {usaha:.2f} J")
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