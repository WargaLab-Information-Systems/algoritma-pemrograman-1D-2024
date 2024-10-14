# meminta input angka dari pengguna 
angka = input("masukkan angka bulat :")

angka_terbalik = ""
i = len (angka) - 1
print(i)

while i >= 0:
    angka_terbalik += angka[i]
    i -= 1 

# menampilkan hasil
print("angka setelah dibalik :" , angka_terbalik)
