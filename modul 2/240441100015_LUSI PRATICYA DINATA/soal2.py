# Data mahasiswa
jaka_skor = 1100
jaka_ipk = 3.5

ida_skor = 1000
ida_ipk = 3.5

# Syarat beasiswa
syarat_skor = 1100
syarat_ipk = 3.0

# Cek apakah Jaka memenuhi syarat
if jaka_skor > syarat_skor and jaka_ipk > syarat_ipk:
    print("Jaka lulus persyaratan beasiswa.")
else:
    print("Jaka tidak lulus persyaratan beasiswa.")

# Cek apakah Ida memenuhi syarat
if ida_skor > syarat_skor and ida_ipk > syarat_ipk:
    print("Ida lulus persyaratan beasiswa.")
else:
    print("Ida tidak lulus persyaratan beasiswa.")
