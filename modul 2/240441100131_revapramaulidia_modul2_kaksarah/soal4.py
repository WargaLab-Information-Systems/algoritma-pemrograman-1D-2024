tahun = int(input("MASUKKAN TAHUN: "))

if (tahun % 400 == 0):
    print("TAHUN TERSEBUT MERUPAKAN TAHUN KABISAT")
elif (tahun % 100 == 0):
    print("TAHUN TERSEBUT BUKAN TAHUN KABISAT")
elif (tahun % 4 == 0):
    print("TAHUN TERSEBUT MERUPAKAN TAHUN KABISAT")
else :
    print("TAHUN TERSEBUT BUKAN TAHUN KABISAT")