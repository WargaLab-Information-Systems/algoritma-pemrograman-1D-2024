size = int(input("Masukkan size: "))

# angka 0
for i in range(size): #baris 
  for ii in range(size): #kolom
     if i == 0 or i == size - 1 or ii == 0 or ii == size - 1 :
      print("x", end=" ")
     else:
      print(" ", end=" ")
  print()
print(" ")

# membuat angka 5
for i in range(size): #baris
    for ii  in range(size): #kolom
        if i == 0 or i == size // 2 or i == size - 1 or (ii == 0 and i < size // 2) or (ii == size - 1 and i > size // 2):
            print("x", end=" ")
        else:
            print(" ", end=" ")
    print()
print(" ")

# membuat angka 5
for i in range(size):
    for ii in range(size):
        if i == 0 or i == size // 2 or i == size - 1 or (ii == 0 and i < size // 2) or (ii == size - 1 and i > size // 2):
            print("x", end=" ")
        else:
            print(" ", end=" ")
    print()
print(" ") 

