# penentuan nilai
nama = input("Masukkan nama :")
nim = input("Masukkan NIM :")
nilai_uts = int(input("Masukkan nilai uts :"))
nilai_uas = int(input("Masukkan nilai: "))

# Nilai rata-rata
nilai_rata_rata = (nilai_uts + nilai_uas) / 2
print("Nilai rata-rata anda :", int(nilai_rata_rata))

if nilai_rata_rata <= 100 >= 81:
    print("Nilai anda A")
elif nilai_rata_rata <=80 >= 71:
    print("Nilai anda B")
elif nilai_rata_rata <=70 >= 61:
    print("Nilai anda C")
elif nilai_rata_rata <=60 >= 41:
    print("Nilai anda D")
elif nilai_rata_rata <=40 >=0:
    print("Nilai anda E")
else:
    print("Nilai tidak masuk ke dalam rata-rata")

# Persyaratan lulus beasiswa
skor = 1100
ipk = 3.0

# Seleksi beasiswa Jaka
nama = input("Masukkan nama :")
skor = int(input("Masukkan skor :"))
ipk = float(input("Masukkan ipk :"))

if skor >= 1100 and ipk >= 3.0:
    print(nama, "telah lulus beasiswa")
else:
    print(nama, "tidak lulus beasiswa")

# Seleksi beasiswa Ida
nama = input("Masukkan nama :")
skor = int(input("Masukkan skor :"))
ipk = float(input("Masukkan ipk :"))

if skor >= 1100 and ipk >= 3.0:
    print(nama, "telah lulus beasiswa")
else:
    print(nama, "tidak lulus beasiswa")

# # Flowchart nomer 2
# <?xml version="1.0"?>
# <flowgorithm fileversion="4.2">
#     <attributes>
#         <attribute name="name" value="Beasiswa"/>
#         <attribute name="authors" value="Bill Cipher"/>
#         <attribute name="about" value=""/>
#         <attribute name="saved" value="2024-10-07 09:32:35 PM"/>
#         <attribute name="created" value="QmlsbCBDaXBoZXI7TEFQVE9QLTNHUFVTOE5MOzIwMjQtMTAtMDY7MDk6NTc6NTkgUE07MzQwNQ=="/>
#         <attribute name="edited" value="QmlsbCBDaXBoZXI7TEFQVE9QLTNHUFVTOE5MOzIwMjQtMTAtMDc7MDk6MzI6MzUgUE07MzszNTAz"/>
#     </attributes>
#     <function name="Main" type="None" variable="">
#         <parameters/>
#         <body>
#             <output expression="&quot;Masukkan nama&quot;" newline="True"/>
#             <declare name="nama" type="String" array="False" size=""/>
#             <input variable="nama"/>
#             <output expression="&quot;Masukkan skor&quot;" newline="True"/>
#             <declare name="skor" type="Integer" array="False" size=""/>
#             <input variable="skor"/>
#             <output expression="&quot;Masukkan ipk&quot;" newline="True"/>
#             <declare name="ipk" type="Real" array="False" size=""/>
#             <input variable="ipk"/>
#             <if expression="ipk &gt;= 3.0 and skor &gt; 1100">
#                 <then>
#                     <output expression="&quot;Selamat, anda lulus beasiswa&quot;" newline="True"/>
#                 </then>
#                 <else>
#                     <output expression="&quot;Maaf, anda tidak lulus beasiswa&quot;" newline="True"/>
#                 </else>
#             </if>
#         </body>
#     </function>
# </flowgorithm>

    # Tahun kabisat
print("Tahun kabisat adalah tahun yang habis dibagi 4, 400, dan tidak habis dibagi 100")

tahun = int(input("Masukkan tahun: "))
if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
  print(tahun, "adalah tahun kabisat")
else:
  print(tahun, "bukan tahun kabisat")

# Diskon
nama_pembeli = input("Masukkan nama pembeli :")
usia_pembeli = int(input("Masukkan usia pembeli :"))
total_belanja = float(input("Masukkan total belanja :"))
kartu_member = input("Apakah anda memiliki kartu member? (ya/tidak):")

if usia_pembeli < 18:
    print("Maaf, usia anda belum mencukupi")
else:
    diskon = 0
    if kartu_member == "ya":
        diskon = 15
    if total_belanja > 500.000:
        diskon = 10
    if kartu_member == "ya" and total_belanja >= 500_000:
        diskon = 25

    # Hitung total diskon
    total_diskon = total_belanja * diskon / 100

    # Hitung total harga setelah diskon
    total_bayar = total_belanja - total_diskon

    print("Rincian Pembayaran")
    print("Nama Pembeli:", nama_pembeli)
    print("Diskon yang didapatkan:", diskon,"%")
    print("Total harga sebelum diskon: Rp", int(total_belanja))
    print("Total harga setelah diskon: Rp", int(total_bayar))