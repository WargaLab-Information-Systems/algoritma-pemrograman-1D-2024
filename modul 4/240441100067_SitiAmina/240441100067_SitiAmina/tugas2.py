desimal = int(input("Masukkan bilangan desimal: "))
biner = ""

while desimal > 0: #loop berjalan selama desimal lebih dari 0
        sisa = desimal % 2
        biner = str(sisa) + biner
        desimal //= 2

for i in range(len(biner)):
        print(biner[:i + 1])