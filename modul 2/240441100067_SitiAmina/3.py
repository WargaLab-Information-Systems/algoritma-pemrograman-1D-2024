#MENENTUKAN TAHUN KABISAT 

#MENGINPUTKAN TAHUN 
print("---------------------")
tahun = int(input("Masukkan Tahun "))
print("---------------------")

#PENYELEKSIAN KONDISI MENGGUNAKAN IF ELIF ELSE DENGAN MEMASUKKAN RUMUS UNTUK MENENTUKAN TAHUN KABISAT
print("*******************************************")
if tahun % 400 == 0 :
    print(tahun , "Merupakan tahun Kabisat")

elif tahun % 100 == 0 :
    print(tahun , "Bukan tahun kabisat")
elif tahun % 4 == 0 :
    print(tahun , "Merupakan tahun kabisat")
else :
    print(tahun, "Bukan merupakan tahun kabisat")
print("*******************************************")


    
