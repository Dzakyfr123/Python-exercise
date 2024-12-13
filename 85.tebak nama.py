#tebak nama
# dibuat pada 13/12/2024
# oleh dzaky fadhilah rahmawan

import random

def game_tebak_nama():
    daftar_nama = ["Andi", "Budi", "Cici", "Dedi", "Eni"]
    nama_rahasia = random.choice(daftar_nama)

    print("Selamat datang di game Tebak Nama!")
    print("Saya sedang memikirkan sebuah nama.")

    tebakan = ""
    while tebakan != nama_rahasia:
        tebakan = input("Tebakan Anda: ")
        if tebakan.lower() == nama_rahasia.lower():
            print("Selamat, Anda benar!")
        else:
            print("Salah, coba lagi!")

game_tebak_nama()