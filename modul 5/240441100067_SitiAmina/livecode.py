daftar = ""
login = ""

while True:
    pilihan = input("Masukkan pilihan Anda :")
    if pilihan == "1":
        print("Anda memilih daftar")
        user =input("Masukkan username:")
        passw =input("Masukkan password:")
        print("Anda berhasil mendaftar")
    
    elif pilihan == "2":
        print("Anda memilih login")
        username =input("Masukkan username:")
        password =input("Masukkan password:")

        if username == user and password == passw:
            print("Anda berhasil login")
        else:
            print("salah woy")
         
