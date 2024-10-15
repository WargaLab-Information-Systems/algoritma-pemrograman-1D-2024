size = int(input("Masukkan size : "))

for baris in range (size +1) :
    for kolom in range(size +1) :
        if (kolom == 0) or (kolom == 6 and (baris !=0 and baris !=7)) or ((baris == 0 or baris == 6) and
           (kolom >0 and kolom<7)) :
            print("x", end="")
        else :
            print(end=" ") #tanpa newline
    print()
for baris in range (size +1) :
    for kolom in range(size +1) :
        if (baris == 3 and kolom < 8) or (kolom == 0 or kolom == 6)and (
            baris > 3 and baris < 8) or (
            kolom == 0 and (baris < 8 and baris > 0)) or (
            baris == 0 and (kolom < 8 and kolom < 8)) or (
            baris == 6 and (kolom > 0 and kolom < 7)):
            print("x", end="")
        else :
            print(end=" ")
    print()
for baris in range (size +1) :
    for kolom in range(size +1) :
        if (baris == 0 and kolom < 8) or (kolom ==6 and baris !=7):
            print("x", end="")
        else  :
            print(end=" ")
    print()





