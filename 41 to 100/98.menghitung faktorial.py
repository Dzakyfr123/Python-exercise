# mennghitung faktorial
#di buat pada 13/12/2024
#oleh dzaky fadhilah rahmawan

def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)

n = int(input("Masukkan bilangan: "))
print("Faktorial dari", n, "adalah", faktorial(n))