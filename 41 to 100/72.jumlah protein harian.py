#jumlah protein
# di buat pada 13/12/2024
# oleh dzaky fadhilah rahmawan

kelamin = str(input("masukan jenis kelamin anda (cowok/cewek) = "))
umur = int(input("masukan umur anda = "))
    
if kelamin == "cowok":
    if 1 <= umur <= 3:
        print("kamu masih anak anak")
        print("protein yang harus kamu konsumsi perhari\n adalah 14 gram") 
    elif 4 <= umur <= 8:
        print("kamu masih anak anak")
        print("protein yang harus kamu konsumsi perhari\n adalah 19 gram") 
    elif 9 <= umur <= 13:
        print("kamu masih anak anak")
        print("protein yang harus kamu konsumsi perhari\n adalah 34 gram") 
    elif 14 <= umur <= 18:
        print("kamu sudah remaja")
        print("protein yang harus kamu konsumsi perhari\n adalah 52 gram") 
    elif 19 <= umur <= 50:
        print("kamu sudah dewasa")
        print("protein yang harus kamu konsumsi perhari\n adalah 56 gram") 
    elif umur < 51:
        print("kamu sudah manula")
        print("protein yang harus kamu konsumsi perhari\n adalah 56 gram") 
elif kelamin == "cewek":
    if 1 <= umur <= 3:
        print("kamu masih anak anak")
        print("protein yang harus kamu konsumsi perhari\n adalah 14 gram") 
    elif 4 <= umur <= 8:
        print("kamu masih anak anak")
        print("protein yang harus kamu konsumsi perhari\n adalah 19 gram") 
    elif 9 <= umur <= 13:
        print("kamu masih anak anak")
        print("protein yang harus kamu konsumsi perhari\n adalah 34 gram") 
    elif 14 <= umur <= 18:
        print("kamu sudah remaja")
        print("protein yang harus kamu konsumsi perhari\n adalah 46 gram") 
    elif 19 <= umur <= 50:
        print("kamu sudah dewasa")
        print("protein yang harus kamu konsumsi perhari\n adalah 46 gram") 
    elif umur < 51:
        print("kamu sudah manula")
        print("protein yang harus kamu konsumsi perhari\n adalah 46 gram")

print("terima kasih")