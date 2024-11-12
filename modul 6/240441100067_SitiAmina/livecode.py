bil1 = 0
bil2 = 0

def tambah (bil1, bil2):
    return bil1 + bil2
def kurang (bil1, bil2):
    return bil1 - bil2
def kali (bil1, bil2):
    return bil1 * bil2
def bagi (bil1, bil2):
    return bil1 / bil2

while True :
    print("1. penjumlahan")
    print("2. pengurangan")
    print("3. perkalian")
    print("4. pembagian")
    print("5. keluar")
    pilih = input("Masukkan pilihan :")
    if pilih == "1":
        bil1 = int(input("Masukkan bilangan pertama :"))
        bil2 = int(input("Masukkan bilangan kedua :"))
        print ("hasil penjumlahan bil1 dan bil2 adalah " , tambah(bil1, bil2))
    elif pilih == "2":
        bil1 = int(input("Masukkan bilangan pertama :"))
        bil2 = int(input("Masukkan bilangan kedua :"))
        print ("hasil pengurangan dari bil1 dan bil2 adalah " , kurang(bil1, bil2))
    elif pilih == "3":
        bil1 = int(input("Masukkan bilangan pertama :"))
        bil2 = int(input("Masukkan bilangan kedua :"))
        print ("hasil perkalian dari bil1 dan bil2 adalah " , kali(bil1, bil2))
    elif pilih == "4":
        bil1 = int(input("Masukkan bilangan pertama :"))
        bil2 = int(input("Masukkan bilangan kedua :"))
        print("Hasil pembagian dari bil1 dan bil2 adalah :", bagi(bil1, bil2))
    elif pilih == "5":
        print ("program selesai") 
        break
    
        
        
        
    

    