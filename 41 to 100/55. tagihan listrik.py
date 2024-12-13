# tagihan listrik
# dibuat pada 13/12/2024
#oleh dzaky fadhilah rahmawan

TARIF = 1500
while True:

    try:
        bulan_pemakaian = float(input("berapa bulan yang anda inginkan = "))
        daya_listrik = float(input("masukan besar daya (w/watt) = "))
        waktu = float(input("berapa total jam pemakaian per bulan = "))
        biaya_listrik = (daya_listrik / 1000) * waktu * TARIF * 30 * bulan_pemakaian
        print(f"biaya listrik rumah anda selama {bulan_pemakaian} bulan = {biaya_listrik:.2f} ")
        while True:
                isdone = str(input("apakah masih mau lagi (y/t) ? = "))
                if isdone == "y":
                    break
                elif isdone == "t":
                    print("terimakasihh program selesai")
                    exit()
                else:
                    print("Input tidak valid. Silakan masukkan 'y' untuk ya atau 't' untuk tidak.")    
    except ValueError:
        print("inputan anda tidak valid")
        print("masukan bilangan bulat / float")
        break
print("TERIMA KASIH")