#database siswa 
# #dibuat pada 31/12/2024
# oleh dzaky fadhilah rahmawan 

import datetime
import random
import string
data_siswa = {} 

while True:
   
    data_template = {
        "nama siswa": "",
        "kelas": "",
        "usia": "",
        "cita cita": "",
        "lahir": datetime.datetime(2000, 11, 11)
    }

    
    siswa = dict.fromkeys(data_template.keys())

    
    siswa["nama siswa"] = input("masukan nama anda = ")
    siswa["kelas"] = input("masukan kelas anda = ")
    siswa["usia"] = input("masukan usia anda = ")
    siswa["cita cita"] = input("masukan cita cita anda = ")
    TAHUN_LAHIR = int(input("masukan tahun lahir = "))
    BULAN_LAHIR = int(input("masukan bulan lahir = "))
    TANGGAL_LAHIR = int(input("masukan tanggal lahir = "))
    siswa["lahir"] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)


    
    KEY = "".join((random.choice(string.ascii_uppercase) for i in range(3)))

    data_siswa[KEY] = siswa 

    

    print(f'{"key":<6} {"nama siswa":<17} {"kelas":<10} {"usia":^15} {"cita cita":<17} {"lahir":^10}')
    for key in data_siswa:
        NAMA = data_siswa[key]["nama siswa"]
        KELAS = data_siswa[key]["kelas"]
        USIA = data_siswa[key]["usia"]
        CITA_CITA = data_siswa[key]["cita cita"]
        LAHIR = data_siswa[key]["lahir"].strftime("%x")
        print("_" * 80)
        print(f"{key:<6} {NAMA:<17} {KELAS:<10} {USIA:^15} {CITA_CITA:<17} {LAHIR:^10}")

    is_done = input("apakah masih ingin ditambah ? (y/t) = ")
    if is_done.lower() == "t":
        break

print("TERIMA KASIH")