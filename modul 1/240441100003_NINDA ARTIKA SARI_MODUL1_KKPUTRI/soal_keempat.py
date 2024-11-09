def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

def kombinasi(n, r):
    return faktorial(n) // (faktorial(r) * faktorial(n - r))

# Total orang dan jumlah yang ingin dipilih
total_orang = 7
jumlah_pilih = 4

# Menghitung jumlah cara
jumlah_cara = kombinasi(total_orang, jumlah_pilih)

print(f"Banyak cara untuk memilih {jumlah_pilih} orang dari {total_orang} orang adalah: {jumlah_cara} adalah")