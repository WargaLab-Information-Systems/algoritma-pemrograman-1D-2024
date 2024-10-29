# Data Jaka
skor_jaka = 1100
ipk_jaka = 3.5

# Data Ida
skor_ida = 1000
ipk_ida = 3.5

# Persyaratan
skor_minimal = 1100
ipk_minimal = 3.0

# Mengecek apakah Jaka lulus persyaratan beasiswa
if skor_jaka >= skor_minimal and ipk_jaka >= ipk_minimal:
    print("Jaka lulus persyaratan beasiswa.")
else:
    print("Jaka tidak lulus persyaratan beasiswa.")

# Mengecek apakah Ida lulus persyaratan beasiswa
if skor_ida >= skor_minimal and ipk_ida >= ipk_minimal:
    print("Ida lulus persyaratan beasiswa.")
else:
    print("Ida tidak lulus persyaratan beasiswa.")