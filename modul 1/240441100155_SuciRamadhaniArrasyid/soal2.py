def jumlah_deret_aritmetika(u5, u8_dan_u12):
  

  # Mencari beda (b) dan suku pertama (a)
  b = (u8_dan_u12 - 2*u5) / 10
  a = u5 - 4*b

  # Menghitung jumlah 8 suku pertama (S8)
  s8 = 8/2 * (2*a + 7*b)
  return s8

# Input nilai yang diketahui
u5 = 11
u8_dan_u12 = 52

# Hitung jumlah 8 suku pertama
hasil = jumlah_deret_aritmetika(u5, u8_dan_u12)

print("Jumlah 8 suku pertama dari deret aritmetika adalah:", hasil)