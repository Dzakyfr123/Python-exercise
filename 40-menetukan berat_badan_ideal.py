#menetukan badan ideal
# di buat pada 17/11/2024
# di buuat oleh Dzaky fadhilah rahmawan



print(30*"=")
print("PROGRAM MENGHITUNG BERAT BADAN")
print(30*"=")

tinggi = int(input("masukan tinggi badan anda = "))

persen = tinggi * 10 / 100
berat_ideal = tinggi - 100 - persen

print(f"ini adalah berat badan ideal untuk anda = {berat_ideal}")