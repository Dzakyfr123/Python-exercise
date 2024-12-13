#berapa lama air mendidih
#di buat pada 13/12/2024
#oleh dzaky fadhilah rahmawan

def eksperimen_mendidih():
  volume_air = float(input("Masukkan volume air (liter): "))
  suhu_awal = float(input("Masukkan suhu awal air (Celcius): "))
  sumber_panas = input("Masukkan jenis sumber panas: ")

  import time
  waktu_awal = time.time()

  print("Memanaskan air...")
  time.sleep(10)  

  waktu_akhir = time.time()
  waktu_mendidih = waktu_akhir - waktu_awal

  print(f"Waktu yang dibutuhkan untuk mendidih: {waktu_mendidih} detik")

 
eksperimen_mendidih()