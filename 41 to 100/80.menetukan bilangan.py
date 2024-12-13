#menetukan bilangan
#di buat pada 13/12/2024
#oleh dzaky fadhilah rahmawan

x = int(input("masukan bilangan bulat 1 = "))
y = int(input("masukan bilangan bulat 2 = "))
z = int(input("masukan bilangan bulat 3 = "))

if x > y and x > z:
    print(f"ini adalah bilangan terbesar {x}")
elif y > x and y > z:
    print(f"ini adalah bilangan terbesar {y}")
elif z > x and z > y:
    print(f"ini adalah bilangan terbesar {z}")
else:
    print()
if x < y and x < z:
    print(f"ini adalah bilangan terkecil {x}")
elif y < x and y < z:
    print(f"ini adalah bilangan terkecil {y}")
elif z < x and z < y:
    print(f"ini adalah bilangan terkecil {z}")