# menghitung tekanan pada benda
#di buat pada 13/12/2024
# oleh dzaky fahilah rahmawan

while True:
    try:
        gaya = float(input("berapa besaran gaya benda (n) = "))
        luas = float(input("berapa luas permukaan benda tempat gaya diterapkan (m2) = "))
        tekanan = gaya / luas
        print(f"tekanan benda ini adalah = {tekanan:.2f} J")
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