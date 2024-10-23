#Soal Nomor 1
#Meminta Ukuran dari Pengguna
size = int(input("Masukkan ukuran: "))

#Membuat Angka 0
for i in range (size):
    if i in range (1): 
        print("x" * size)
    elif i in range(size - 1, size): 
        print("x" * size)
    else: 
        print("x" + " " * (size - 2) + "x")

print()

#Membuat Angka 7
for i in range (size):
    if i in range (1): 
        print("x" * size)
    elif i in range (0, size): 
        print(" " * (size - i - 1) + "x")

print()

#Membuat Angka 1
for i in range (size):
    if i in range (size):
        print(" " * (size - 1) + "x")