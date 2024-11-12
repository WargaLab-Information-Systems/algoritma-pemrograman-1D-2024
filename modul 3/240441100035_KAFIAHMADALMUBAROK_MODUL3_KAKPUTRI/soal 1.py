 # membuat pola angka sesuai nim
n = int(input("masukan size: "))

# pola 0
for i in range(n): # membuat angka nol
    if i == 0:
        print("0" * n)  # batas atas # baris
    elif i == n-1:
        print("5" * n)  # batas bawah # baris
    else:
        print("3"+" " * (1*(n-2))+"3") # batas kanan dan kiri # kolom

print()

# membuat pola 3
for i in range (n): # membuat angka 3
    if i == 0:
        print("0" * n) # batas atas
    elif i == n // 2:
        print("3" * n) # batas tengah
    elif i == n - 1:
         print("5" * n) # batas bawah
    else:
        print (""+" "* (n-2)+" ""0") # batas kanan

print()

#  membuat pola 5
for i in range(n):
    if i == 0:
        print("0" * n) # batas atas
    elif i == n // 2:
        print("3" * n) # batas tengah
    elif i == n-1:
        print("5" * n) # batas bawah
    elif i< n // 2:
        print("0") # batas kiri
    else:
        print(" " * (1*(n-1))+ "0") # batas kanan bawah

print()
 