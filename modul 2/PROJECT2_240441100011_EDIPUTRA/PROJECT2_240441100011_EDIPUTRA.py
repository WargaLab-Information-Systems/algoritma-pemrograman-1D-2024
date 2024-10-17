#Soal no 1
nama = input("Masukkan Nama Anda: ")
nim = input("Masukkan NIM Anda: ")
uts = float(input("Masukkan Nilai UTS Anda: "))
uas = float(input("Masukkan Nilai UAS Anda: "))

r = (uts + uas) / 2
if r > 81 and r <= 100:
    nilai = "A"
elif r > 71 and r <= 80:
    nilai = "B"
elif r > 61 and r <= 70:
    nilai = "C"
elif r > 41 and r <= 60:
    nilai = "D"
elif r == 0 and r <=40:
    nilai = "E"
else:
    nilai = "yang tidak sesuai"


print(f"Nama Anda:{nama}")
print(f"NIM Anda:{nim}")
print(f"Nilai rata-rata anda:{r}")
print(f"Anda mendapatkan Nilai {nilai}")


# Soal no 2
jaka_skor = 1100
jaka_ipk = 3.5
ida_skor = 1000
ida_ipk = 3.5

# Persyaratan beasiswa
syarat_skor = 1100
syarat_ipk = 3.0

# Penyeleksian kondisi beasiswa
if jaka_skor > syarat_skor and jaka_ipk >= syarat_ipk:
    print("Jaka lulus persyaratan beasiswa.")
else:
    print("Jaka tidak lulus persyaratan beasiswa.")

if ida_skor > syarat_skor and ida_ipk >= syarat_ipk:
    print("Ida lulus persyaratan beasiswa.")
else:
    print("Ida tidak lulus persyaratan beasiswa.")


#soal no 4
tahun = int(input("masukan tahun: "))

if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(f"{tahun} adalah tahun kabisat")
else:
    print(f"{tahun} bukan tahun kabisat")


#Soal no 5
nama = input("Masukkan nama: ")
member = input("Apakah Anda memiliki kartu member? (ya/tidak): ")
total = float(input("Masukkan total belanja: "))
usia = int(input("Masukkan usia: "))

if usia < 18:
    print("Maaf, usia Anda belum mencukupi.")
else:
    diskon_member = 0
    diskon_belanja = 0

    if member == "ya":
        diskon_member = 15 

    if total > 500000:
        diskon_belanja = 10
    
    total_diskon = diskon_member + diskon_belanja
    if total_diskon > 0:
        total_setelah_diskon = total - (total * total_diskon / 100)
    else:
        total_setelah_diskon = total
    
    print(f"Nama Pembeli: {nama}")
    print(f"Total Diskon: {total_diskon}%")
    print(f"Total Harga Sebelum Diskon: Rp{total}")
    print(f"Total Harga Setelah Diskon: Rp{total_setelah_diskon}")