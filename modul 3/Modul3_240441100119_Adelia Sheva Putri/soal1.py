#mencetak angka 1
size = int(input("masukkan size: "))
for baris in range(size):
    if baris == 0:
        print(" ","XX","   ")
    if baris == 1:
        print("","X","X","   ")
    if baris == 2 or baris == 3 or baris == 4:
        print("  ","X")
    if baris == 5:
        print("","XXXXX")


#mencetak angka 1
for baris in range(size):
    if baris == 0:
        print(" ","XX","   ")
    if baris == 1:
        print("","X","X","   ")
    if baris == 2 or baris == 3 or baris == 4:
        print("  ","X")
    if baris == 5:
        print("","XXXXX")

#mencetak angka 9
for baris in range(size):
    if baris == 0:
        print("XXXXXX")
    if baris == 1:
        print("X","  ","X")
    if baris == 2:
        print("XXXXXX")
    if baris == 3 or baris == 4:
        print("    ","X")
    if baris == 5:
        print("XXXXXX")




# size = int(input("masukkan size: "))
# for i in range(size):
#         if i == 0 or i == 4 or i == 9:
#             print("X" * size)
#         if i == 1 or i == 2 or i == 3:
#             print("X"+" "*(size - 2) + "X")
#         if i == 5 or i == 6 or i == 7 or i == 8:
#             print(" "*(size - 1)+"X")

# for i in range(size):
#         if i == 0:
#             print(" "*(size-7)+("X"*2)+" "*(size-3))
#         if i == 1:
#             print(" "*(size-8)+"X"+" "*(size-9)+"X")
#         if i == 2 or i == 3 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8:
#             print(" " * (size-6) + "X" + " " * (size-2))
#         if i == 9:
#             print("X"*(size-1))
    
# for i in range (size):
#      if i == 0 or i == 5 or i == 9:
#           print("X"*(size))
#      if i == 1 or i == 2 or i == 3 or i == 5 or i == 6 or i == 7 or i  == 8:
#           print(" "*(size- 1)+ "x")

# for i in range (size):
#      if i == 0 or i == 1 or i == 2 or i == 3:
#           print ("X"+ " "*(size - 2)+"X")
#      if i == 4:
#           print ("X"*(size))
#      if i == 6 or i == 7 or i == 8 or i == 9:
#           print (" "*(size - 1)+ "X")
    

          