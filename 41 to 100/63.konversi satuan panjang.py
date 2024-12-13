#konversi satuan panjang
# di buat pada 13/12/2024
# oleh dzaky fadhilah rahmawan

while True:
    try:
        inputan = int(input("masukan satuan meter = "))
        mllimeter = inputan * 1000
        sentimeter = inputan * 100
        dekameter = inputan % 10
        hektometer = inputan % 100
        kilometer = inputan % 1000
        print(f"""hasil konversi meter {inputan}\nmilimeter = {mllimeter}\nsentimeter = {sentimeter}\ndekameter = {dekameter}\nhektometer = {hektometer}\nkilometer = {kilometer}""")
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
        print("masukan inputan bertipe integer saja")