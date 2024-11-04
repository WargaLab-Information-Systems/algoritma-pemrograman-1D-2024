desimal = int(input("bilangan desimal: "))
biner = ""
while desimal > 0:
    sisa = desimal % 2
    biner += str(sisa)
    desimal //= 2
biner = biner [::-1]
for i in range(1,len(biner)+1):
    print(biner[:i])