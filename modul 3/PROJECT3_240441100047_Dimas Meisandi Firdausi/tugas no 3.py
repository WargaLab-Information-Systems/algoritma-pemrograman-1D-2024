## SOAL NO 3


# Program untuk menghitung denda keterlambatan DVD
while True:
  # Meminta input lama waktu penyewaan dari pengguna
  lama_sewa = int(input("Lama waktu penyewaan (hari): "))

  # Menghitung lama keterlambatan
  lama_terlambat = lama_sewa - 5

  # Inisialisasi denda
  denda = 0

  # Menghitung denda jika DVD terlambat
  if lama_terlambat > 0:
    denda += lama_terlambat * 2500 # Denda harian

    # Denda tambahan per 5 hari jika terlambat lebih dari 10 hari
    if lama_terlambat > 10:
      denda += ((lama_terlambat - 10) // 5) * 5500

  # Menampilkan hasil perhitungan
  if lama_terlambat > 0:
    print(f"DVD terlambat dikembalikan selama {lama_terlambat} hari.")
    print(f"Total denda: Rp{denda:,}")
  else:
    print("DVD dikembalikan tepat waktu. Tidak ada denda.")

  # Menanyakan apakah user ingin menghitung lagi
  lanjut = input("Hitung lagi? (ya/tidak): ").lower()
  if lanjut  != 'ya':
    break 
print("Terima kasih telah menggunakan program ini!")  