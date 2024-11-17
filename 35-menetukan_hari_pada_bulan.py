#menentukan hari pada bulan
# di buat pada 17/11/2024
# di buat oleh Dzaky fadhilah rahmawan


print(30*"=")
print("PROGRAM MENENTUKAN HARI DALAM BULAN")
print(30*"=")

menu_bulan = {
    "januari"  : 31,
    "februari" : 29,
    "maret"    : 31,
    "april"    : 30,
    "mei"      : 31,
    "juni"     : 30,
    "juli"     : 31,
    "agustus"  : 31,
    "september": 30,
    "oktober"  : 31,
    "november" : 30,
    "desember" : 31
}
for bulan,hari in menu_bulan.items():
    print(f"bulan = {bulan}, jumlah hari = {hari}")

input_user = str(input("masukan nama bulan = "))

print(f"{bulan} yang anda pilih punya = {hari} hari")