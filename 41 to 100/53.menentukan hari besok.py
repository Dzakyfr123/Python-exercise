# menentukan hari selanjutnya
# pada 13/12/2024
# di buat oleh dzaky fadhilah rahmawan


daftar_hari = ["senin","selasa","rabu","kamis","jumat","sabtu","minggu"]

def display_hari():
    for no,hari in enumerate(daftar_hari,start=1):
        print(f"{no}. hari = {hari}")
    
while True:
    try:
        print(f"SILAHKAN PILIH HARI")
        display_hari()
        hari_pertama = str(input("masukan hari pertama = "))
        jumlah = int(input("berapa hari setelahnya ? = "))
        hasil = jumlah % 7
        if hari_pertama not in daftar_hari:
            print("inputan anda tidak valid")
            continue
        index_hari_pertama = daftar_hari.index(hari_pertama)
        
        index_hari_setelah = (index_hari_pertama + (jumlah % 7))%7
        
        hari_setelah = daftar_hari[index_hari_setelah]
        print(f"{jumlah} hari setelah hari {hari_pertama} adalah = {hari_setelah}")
        
        while True:
            isdone = str(input("apakah masih mau lagi (y/t) ? = "))
            if isdone == "y":
                break
            elif isdone == "t":
                print("TERIMA KASIH")
                exit()
            else:
                print("silahkan masukan (y/t) saja")
                break
    except ValueError:
        print("inputan anda tidak valid")
        break