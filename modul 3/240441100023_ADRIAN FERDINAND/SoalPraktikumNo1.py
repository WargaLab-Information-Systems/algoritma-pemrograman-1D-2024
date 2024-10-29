size = int(input("Masukkan size: "))

# angka 0
for i in range(size):
  for ii in range(size):
     if i==0 or i==size-1 or ii==0 or ii==size-1 :
      print("x", end="")
     else:
      print(" ", end="")
  print()
print()


# angka 2
for i in range(size):
    for ii in range(size):
        if i==0 or i==size//2 or i==size-1 or ( ii==size-1 and i < size//2) or ( ii==0 and i > size//2 ):
            print("x", end="")
        else:
            print(" ", end="")
    print()
print()


# angka 3
for i in range(size):
    for ii in range(size):
        if i==0 or i==size//2 or i==size-1 or ( ii==size-1) :
            print("x", end="")
        else:
            print(" ", end="")
    print()
print()