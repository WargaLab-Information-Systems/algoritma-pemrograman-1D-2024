# Soal Nomor 3
# Program Menghitung Faktorial

def menghitung_faktorial(n):
    if n < 0:
        return "Mohon maaf, angka tidak terdefinisi"
    elif n == 0 or n == 1:
        return 1
    else:
        hasil = 1
        for okjohjhjhjhjkhk in range(2, n + 1):
            hasil *= okjohjhjhjhjkhk
        return hasil

# Meminta input dari pengguna
angka_faktorial = int(input("Masukkan angka: "))
print(f"Hasil dari {angka_faktorial}! adalah {menghitung_faktorial(angka_faktorial)}")