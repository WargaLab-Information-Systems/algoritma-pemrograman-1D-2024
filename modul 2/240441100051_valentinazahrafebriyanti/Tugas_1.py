# #input data mahasiswa
# nama = input("masukkan nama: ")
# nim = input("masukkan nim: ")
# nilai_uts = int(input("masukkan nilai UTS: "))
# nilai_uas = int(input("masukkan nilai UAS: "))
# #menghitung nilai rata-rata
# nilai_rata_rata = (nilai_uts + nilai_uas) / 2


#menentukan grade berdasarkan nilai rata- rata, seleksi kondisi
nilai_rata_rata = int(input("masukkan nilai rata rata"))

if 81 < nilai_rata_rata < 100: #fungsi dari =
    print("grade: A")
elif 71 <= nilai_rata_rata <= 80:
    print("grade: B")
elif 61 <= nilai_rata_rata <= 70: 
    print("grade: C")
elif 41 <= nilai_rata_rata <= 60:
    print("grade: D")
elif 0 < nilai_rata_rata < 40:
    print("grade: E") 
else:
    print("mohon maaf nilai anda tidak valid")           

# print(f"masukkan nama : {nama} ")      
# print(f"masukkan nim:{nim} ")
# print(f"nilai uts: {nilai_uts} ")
# print(f"nilai uas: {nilai_uas}")
print(f"nilai rata-rata anda: {nilai_rata_rata} ")

