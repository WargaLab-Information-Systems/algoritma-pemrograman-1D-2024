# Program untuk menentukan tahun kabisat

# Meminta input dari pengguna
tahun = int(input("Masukkan tahun: "))

# Seleksi kondisi untuk menentukan apakah tahun kabisat
if (tahun % 400 == 0):  
    print("tahun tersebut termasuk tahun kabisat")
elif (tahun % 100 == 0):
    print("tahun tersebut bukan tahun kabisat")
elif (tahun % 4 == 0):
    print("tahun teresbut merupakan tahun kabisat")
else :
    print("tahun tersebut bukan tahun kabisat")