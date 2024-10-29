n = int(input("Masukkan bilangan desimal: "))
konvers = n
biner = "" 
while n > 0:
    biner = str(n%2) + biner
    n = n//2
print("Hasil dari konver dari desimal ",konvers ,"ke biner adalah", biner)
print("Pola Segitiga")
for i in range(1, len(biner)+1):
    for j in range(len(biner)-2):
        print(' ', end=' ')
    for k in range(i):
        print(biner[k], end=' ')
    print()