#pengingat waktu
#dibuat pada 13/12/2024
#oleh dzaky fadhilah rahmawan

import time
import datetime

def pengingat_waktu():
    waktu_mulai = datetime.datetime.now()
    durasi_menit = int(input("Berapa menit Anda ingin dibatasi? "))
    waktu_selesai = waktu_mulai + datetime.timedelta(minutes=durasi_menit)

    while datetime.datetime.now() < waktu_selesai:
        print("Jangan lupa istirahat dari HP!")
        time.sleep(60)

pengingat_waktu()