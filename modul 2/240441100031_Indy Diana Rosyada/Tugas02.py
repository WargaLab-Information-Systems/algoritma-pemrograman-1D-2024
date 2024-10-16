# Data Mahasiswa
jaka_skor = 1100
jaka_ipk = 3.5

ida_skor = 1000
ida_ipk = 3.5
# Cek kelulusan beasiswa untuk Jaka
if jaka_skor > 1100 and jaka_ipk >= 3.0:
    print("Jaka lulus persyaratan beasiswa.")
else:
    print("Jaka tidak lulus persyaratan beasiswa.")

# Cek kelulusan beasiswa untuk Ida
if ida_skor > 1100 and ida_ipk >= 3.0:
    print("Ida lulus persyaratan beasiswa.")
else:
    print("Ida tidak lulus persyaratan beasiswa.")