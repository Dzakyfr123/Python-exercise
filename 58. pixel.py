#pixel
#di buat pada 13/12/2024
#oleh dzaky fadhilah rahmmawan

p = float(input("masukan nilai pixel = "))
def n_pixel(p):
    if p > 255:
        return 255
    elif p < 0:
        return 0 
    else:
        return p 
print(f"nilai {p} = {n_pixel(p)} pixel")