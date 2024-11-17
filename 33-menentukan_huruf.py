#menetukan huruf kosonan
# di buat pada 17/11/2024
# Di buat oleh Dzaky fadhilah rahmawan


huruf = str(input("masukan abjad dari A - Z = "))
vokal = ['a','i','u','e','o']
konsonan = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','u','v','w','x','y','z']
bukan_huruf = [vokal,konsonan]
if huruf in vokal:
    print(f"{huruf} merupakan huruf vokal")
elif huruf in konsonan:
    print(f"{huruf} merupakan huruf konsonan")   
elif huruf not in bukan_huruf:
    print(f"{huruf} bukan huruf")