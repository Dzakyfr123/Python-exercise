# program menghitung gajih
# di buat pada 17/11/2024
# di buat oleh dzaky fadhilah rahmawan
print(30*"\033[92m=")
print("PROGRAM MENGHITUNG UPAH KERJA BERDASARKAN JAM")
print(30*"\033[92m=")

golongan_kerja = {
    "pelayan"   : 4000,
    "dokter" : 5000,
    "designer"   : 6000,
    "programmer"       : 7000
}
for golongan,upah in golongan_kerja.items():
    print(f"golongan = {golongan}, upah = {upah}")

input_golongan = str(input("pilih golongan pekerjaan anda = "))
jam_kerja = int(input("masukan durasi bekerja anda = "))

upah_user = golongan_kerja[input_golongan] * jam_kerja
print(f"upah anda adalah = {upah_user}")