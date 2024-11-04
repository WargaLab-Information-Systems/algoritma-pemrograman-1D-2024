# Data Mahasiswa
jaka_skor = 1100
jaka_ipk = 3.5

ida_skor = 1000
ida_ipk = 3.5

# Syarat beasiswa
minimal_skor = 1100
minimal_ipk = 3.0

# Mengecek siapa yang memenuhi syarat
if jaka_skor > minimal_skor and jaka_ipk >= minimal_ipk:
    print("Jaka tidak lulus persyaratan beasiswa.")
else:
    print("Jaka tidak lulus persyaratan beasiswa.")

if ida_skor > minimal_skor and ida_ipk >= minimal_ipk:
    print("Ida lulus persyaratan beasiswa.")
else:
    print("Ida tidak lulus persyaratan beasiswa.")