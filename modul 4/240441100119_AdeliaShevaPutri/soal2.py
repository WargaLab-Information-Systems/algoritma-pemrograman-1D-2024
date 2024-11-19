desimal = int(input("Masukkan bilangan desimal: "))
biner = "" 
while desimal > 0:
    sisa = desimal % 2
    biner = str(sisa) + biner 
    print(biner)
    desimal //= 2  
5