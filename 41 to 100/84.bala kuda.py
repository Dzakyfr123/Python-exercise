#balap kuda
# di buat pada 13/12/2024
# oleh dzaky fadhilah rahmawan

import random

def balap_kuda(jumlah_kuda, panjang_lintasan):
  """Simulasi balap kuda sederhana.

  Args:
    jumlah_kuda: Jumlah kuda yang ikut balapan.
    panjang_lintasan: Panjang total lintasan balapan.
  """

  posisi_kuda = [0] * jumlah_kuda

  kecepatan_kuda = [random.randint(1, 10) for _ in range(jumlah_kuda)]

  while max(posisi_kuda) < panjang_lintasan:
    for i in range(jumlah_kuda):
      posisi_kuda[i] += kecepatan_kuda[i]

    print(posisi_kuda)

  pemenang = posisi_kuda.index(max(posisi_kuda))
  print(f"Kuda {pemenang+1} memenangkan balapan!")

jumlah_kuda = 5
panjang_lintasan = 100
balap_kuda(jumlah_kuda, panjang_lintasan)