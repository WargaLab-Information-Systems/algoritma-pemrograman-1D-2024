# Fungsi untuk mencari nilai a dan d
def hitung_a_d():
    # Persamaan 1: a + 4d = 11
    # Persamaan 2: 2a + 18d = 52
    
    # Nilai dari persamaan 1
    a_plus_4d = 11
    
    # Nilai dari persamaan 2
    dua_a_plus_18d = 52
    
    # Mencari d dengan mengurangi dua_a_plus_18d dengan dua kali a_plus_4d
    d = (dua_a_plus_18d - 2 * a_plus_4d) / 10
    
    # Mencari a dengan mengganti nilai d di persamaan a_plus_4d
    a = a_plus_4d - 4 * d

    return a, d

# Fungsi untuk menghitung jumlah n suku pertama
def hitung_jumlah_suku(a, d, n):
    # Rumus untuk jumlah n suku pertama dari deret aritmatika
    return (n / 2) * (2 * a + (n - 1) * d)

# Hitung nilai a dan d
a, d = hitung_a_d()

# Jumlah suku yang ingin dihitung
n = 8

# Menghitung jumlah 8 suku pertama
jumlah_8_suku_pertama = hitung_jumlah_suku(a, d, n)

# Menampilkan hasil akhir
print(f"Jumlah 8 suku pertama dari deret aritmatika tersebut adalah {jumlah_8_suku_pertama}.")
