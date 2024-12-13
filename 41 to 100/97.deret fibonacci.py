#deret fibonacci
#dibuat pada 13/12/2024
#oleh dzaky fadhilah rahmawan

def fibonacci(n):
    if n <= 0:
        print("Masukkan bilangan positif")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Masukkan jumlah suku: "))
print(fibonacci(n))