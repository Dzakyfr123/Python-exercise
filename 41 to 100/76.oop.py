#oop
#  di buat pada 13/12/2024
# oleh dzaky fadhilah rahmawan

print(f"nilai __name__ pada fungsi.py = '{__name__}'")
def fungsi_tambah(a:int,b:int)->int:
    return a+b
if __name__ == "__main__":
    angka_1 = int(input("masukan nilai 1 = "))
    angka_2 = int(input("masukan nilai 2 = "))
    hasil = fungsi_tambah(angka_1,angka_2)
    print(f"hasil tambah = {hasil}")