def penjumlahan():
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    jumlah = angka1 + angka2
    print("Hasil penjumlahan:", jumlah)

def pengurangan():
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    hasil = angka1 - angka2
    print("Hasil pengurangan:", hasil)

def perkalian():
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    hasil = angka1 * angka2
    print("Hasil perkalian:", hasil)

def pembagian():
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    if angka2 !=0:
        hasil = angka1 / angka2
        print("Hasil pembagian:", hasil)
    else:
        print("tidak terdefinisi bg")
     
while True:
    print("Silakan masukkan pilihan anda")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")
    
    pilihan = input("Masukkan pilihan 1/2/3/4/5: ")
    
    if pilihan == "1":
        penjumlahan()
    elif pilihan == "2":
        pengurangan()
    elif pilihan == "3":
        perkalian()
    elif pilihan == "4":
        pembagian()
    elif pilihan == "5":
        print("dh selesai ngab.")
        break
    else:
        print("Pilihan tidak ada bg. Coba lagi.")
