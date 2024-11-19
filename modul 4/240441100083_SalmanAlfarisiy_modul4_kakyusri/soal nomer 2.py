
desimal = int(input("Masukkan bilangan desimal: "))
biner = ""

while desimal > 0:
    biner =str(desimal % 2) + biner
    desimal = desimal // 2

print("Bilangan biner:", biner)

# for i in range (1,len(biner)+1):
#     for j in range (len(biner)-i):
#         print("   ", end= "")

#     for k in range (1, i+1):
#         print("",biner, end= "")
#     print()