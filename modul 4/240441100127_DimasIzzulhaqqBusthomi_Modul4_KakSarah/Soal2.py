desimal = int(input("Masukkan bilangan desimal: "))
biner = ""

while desimal > 0:
    biner = str(desimal % 2) + biner 
    desimal //= 2  
    print(biner)
