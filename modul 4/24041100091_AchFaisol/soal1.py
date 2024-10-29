n = int(input("masukan size "))
bentuk = input("X/O: ")
for i in range(1, n+1):
  for j in range(n-i):
    print(" ",end="")
  for j in range(1, i+1):
    print(bentuk, end=" ")
  print()

for i in range(n-1,-1,-1):
  for j in range(n-i):
    print(" ",end="")
  for j in range(1, i+1):
    print(bentuk, end=" ")
  print()