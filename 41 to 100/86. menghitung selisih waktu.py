#menghitung selisih waktu
#di buat pada 13/12/2024
# oleh dzaky fadhilah rahmawan
from datetime import datetime, timedelta

tanggal_lahir = datetime(2000, 1, 1)
hari_ini = datetime.now()

selisih_hari = hari_ini - tanggal_lahir
print(f"Usia Anda adalah {selisih_hari.days} hari")