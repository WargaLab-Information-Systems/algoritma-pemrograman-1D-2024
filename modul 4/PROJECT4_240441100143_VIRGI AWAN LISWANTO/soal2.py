desimal = int(input("Masukkan bilangan desimal: "))
biner = ""
if desimal == 0:
    biner = "0"
else:
    while desimal > 0:
        biner = str(desimal % 2) + biner
        desimal //= 2
panjang = 0
for i in biner:
    panjang += 1

for i in range(1, panjang + 1):
    spasi = ' ' * (panjang - i)
    print(spasi+biner[:i])