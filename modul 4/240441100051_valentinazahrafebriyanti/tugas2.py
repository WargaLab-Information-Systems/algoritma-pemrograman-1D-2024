
angka_desimal = int(input("masukkan bilangan desimal: "))
# Konversi bilangan desimal ke biner
biner = ""
if angka_desimal == 0:
    biner = "0"
else:
    while angka_desimal > 0:
        biner = str(angka_desimal % 2) + biner  # Menambahkan di depan
        angka_desimal //= 2  # Mengurangi dengan dibagi 2

# Pola segitiga
i = 0  
while True:
    if biner:
        print(biner[:i + 1])  # Mencetak biner 0 hingga indeks i
        i += 1  # Menaikkan indeks
        if biner[i:i + 1] == "":  
            break  # Jika tidak ada karakter, keluar dari loop
    else:
        break  # Jika biner kosong, keluar dari loop