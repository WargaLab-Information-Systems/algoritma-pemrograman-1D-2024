def jumlah_suku_aritmatika():
    # Diketahui
    d = 3
    a = -1
    
    # Menghitung jumlah dari 8 suku pertama
    n = 8
    S_n = (n / 2) * (2 * a + (n - 1) * d)
    
    return S_n

# Panggil fungsi dan cetak hasilnya
jumlah_8_suku = jumlah_suku_aritmatika()
print(f"Jumlah nilai dari 8 suku pertama adalah: {jumlah_8_suku}")
