## SOAL NO 1


# Meminta pengguna untuk memasukkan ukuran angka
size = int(input("Masukkan ukuran angka (minimal 7 ): "))

for i in range(size): #baris 
  for ii in range(size): #kolom
     if i == 0 or i == size - 1 or ii == 0 or ii == size - 1 :
      print("x", end=" ")
     else:
      print(" ", end=" ")
  print()
print(" ")

# Cetak angka 4
for i in range(size):
    if i == size // 2:  # Baris tengah
        print("hhhhhh")  # Baris penuh
    elif i < size // 2:
        print("h    h")  # 'h' di kedua sisi untuk bagian atas
    else:
        print("     h")  # 'h' hanya di sisi kanan untuk bagian bawah

print()  # Spasi antar angka

# Cetak angka 7
for i in range(size):
    if i == 0:  # Baris pertama penuh
        print("xxxxxxx")  # Baris penuh
    elif i < size:  # Baris miring
        print(" " * (size - i) + "x")  # 'x' bergerak ke kanan
