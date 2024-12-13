# menuliskan hal berulang
#di buat pada 13/12/2024
#oleh dzaky fadhila rahmawan

print(f"apa yang kamu fikir kan ?")
inputan = str(input("masukan jawaban anda = "))
if inputan == "putri":
    for i in range(1, 101):
        print(f"{i}.lupakan saja, dia bukan milikmu")
else:
    print(f"bagus, fikirkan saja {inputan}")