#sistem penjualan Tiket wisata UTM PARK
kumpulan_paket = [] #menampung data paket yang dibeli
data_pribadi = [] #menampung data pembeli
data_login = [] #menampung data login
data_pembelian = {'jumlah':0,'jumlah1':0,'jumlah2':0,'jumlah3':0,'untung':0, 'untung1':0,'untung2':0,'untung3':0}
date = {'nama':'','tanggal':''}
stok_paket ={"1": 100, "2": 100, "3": 100}

def daftar():
    while True :
        print("\nWELCOME TO PROGRAM PEMESANAN TIKET UTM PARK")
        print("1.Daftar ")
        print("2.Login ")

        login = input("Pilih salah satu(1/2): ")

        while login == "":
            print("input tidak boleh kosong harap masukkan kembali!...")
            login = input("pilih salah satu(1/2): ")
            

        if login == "2":
            print("anda harus daftar terlebih dahulu sebelum login ")       
        elif login == "1":
            print("Anda Memilih daftar")
            username = input("Username : ")
            while username == "":
                print("username tidak boleh kosong!!")
                username = input("Username: ")

            password = input("Password : ")
            while password == "":
                print("password tidak boleh kosong!!")
                password = input("Password: ")

            data_login.append(username)
            data_login.append(password)

            print("\nAkun berhasil TERDAFTAR")
            break
            
def login():
    while True:
        print("\nWELCOME TO PROGRAM PEMESANAN TIKET UTM PARK")
        print("1.Daftar ")
        print("2.Login ")
        login = input("Pilih salah satu(1/2): ")
        if login == "1":
            print("anda sudah mendaftar silahkan login...")
        elif login == "2":
            print("Anda Memilih Login ")
            user = input("Username : ")
            while user == "":
                print("harap masukkan username...")
                user = input("username: ")
            sandi = input("Password : ")
            while sandi == "":
                print("harap masukkan password...")
                sandi = input("masukkan password: ")

            if user != data_login[0]:
                print("Username atau Password (salah / tidak di isi) harap masukkan yang benar...")
            elif sandi != data_login[1] :
                print("Username atau Password (salah / tidak di isi) harap masukkan yang benar...")
            else:
                print("\nAnda berhasil login!!")
                break


def paket_satu():
    while True:
        print("\nHARGA PAKET 1 adalah 100.000/Orang")
        konfirmasi = input ("apakah masih ingin membeli paket 1 (ya/tidak) : ")

        if konfirmasi.lower() == "ya":
           
            nama = input ("\nNama pemesan : ")
            while nama == "":
                print("harap masukkan nama...")
                nama =input("Nama pemesan: ")

            while True:
                try:
                    jumlah = input("Pesen berapa tiket: ")
                    
                    if jumlah == "":
                        print("Harap masukkan jumlah tiket.")
                        continue 
                    jumlah = int(jumlah)
                    break  

                except ValueError:
                    print("Input tidak valid! Harap masukkan angka yang benar untuk jumlah tiket.")
    
            tanggal = str(input("Tanggal wisata (format: DD-MM-YYYY): "))
            while tanggal == "":
                print("harap masukkan tanggal...")
                tanggal = input("Tanggal wisata (format: DD-MM-YYYY): ")
                break
            date['nama'] = nama
            date['tanggal'] = tanggal
            data_pembelian['jumlah'] = jumlah
            if jumlah > stok_paket["1"]:
                data_pembelian['jumlah1'] 
            elif jumlah <= stok_paket['1']:
                data_pembelian['jumlah1'] += jumlah
            
            if stok_paket["1"] < jumlah:
                print("\n Maaf Stok tidak mencukupi, stok yang tersedia:", stok_paket["1"])
                break

            stok_paket["1"] -= jumlah

            hasil = jumlah * 100000 
            data_pembelian['untung1'] = hasil
            data_pembelian['untung'] = hasil

            if jumlah > 20 :
                diskon = 10
                hitung_diskon = hasil * diskon // 100
                mendapat_diskon = hasil - hitung_diskon
                data_pembelian['untung1'] = mendapat_diskon
                data_pembelian['untung'] = mendapat_diskon
                print("Harga sebelum diskon: ",hasil)
                print("Harga sesudah diskon: ", mendapat_diskon, "mendapatkan diskon sebesar",diskon,"% !!")
            else :
                print("Total yang harus dibayar : ",hasil)

            card()
            break
        elif konfirmasi != "tidak":
            print("inputkan yang benar (ya/tidak)")
        else:
            print("\nSilahkan Pilih paket yang lain ")
            break

def paket_dua():
    while True:
        
        print("\nHARGA PAKET 2 adalah 200.000/Orang")
        konfirmasi = input ("apakah masih ingin membeli paket 2 (ya/tidak) : ")

        if konfirmasi.lower() == "ya":
            nama = input ("\nNama pemesan : ")
            while nama == "":
                print("harap masukkan nama...")
                nama =input("Nama pemesan: ")

            while True:
                try:
                    jumlah = input("Pesen berapa tiket: ")
                    
                    if jumlah == "":
                        print("Harap masukkan jumlah tiket.")
                        continue 
                    jumlah = int(jumlah)
                    break  
                except ValueError:
                    print("Input tidak valid! Harap masukkan angka yang benar untuk jumlah tiket.")

            tanggal = str(input("Tanggal wisata (format: DD-MM-YYYY): "))
            while tanggal == "":
                print("harap masukkan tanggal...")
                tanggal = input("Tanggal wisata (format: DD-MM-YYYY): ")
                break

            date['nama'] = nama
            date['tanggal'] = tanggal
            data_pembelian['jumlah'] = jumlah

            if jumlah > stok_paket["2"]:
                data_pembelian['jumlah2'] 
            elif jumlah <= stok_paket['2']:
                data_pembelian['jumlah2'] += jumlah 

            if stok_paket["2"] < jumlah:
                print("\n Maaf Stok tidak mencukupi, stok yang tersedia:", stok_paket["2"])
                break

            stok_paket["2"] -= jumlah

            hasil = jumlah * 200000 
            data_pembelian['untung2'] = hasil
            data_pembelian['untung'] = hasil

            if jumlah > 20 :
                diskon = 10
                hitung_diskon = hasil * diskon // 100
                mendapat_diskon = hasil - hitung_diskon
                data_pembelian['untung2'] = mendapat_diskon
                data_pembelian['untung'] = mendapat_diskon
                print("Harga sebelum diskon: ",hasil)
                print("Harga sesudah diskon: ", mendapat_diskon, "mendapatkan dison sebesar",diskon,"%!!")
            else :
                print("Total yang harus dibayar : ",hasil)

            card()
            break
        elif konfirmasi != "tidak":
            print("inputkan yang benar")
        else:
            print("\nSilahkan Pilih paket yang lain")
            break

def paket_tiga():
    while True:
        
        print("\nHARGA PAKET 3 adalah 300.000/Orang")
        konfirmasi = input ("apakah masih ingin membeli paket 3 (ya/tidak) : ")

        if konfirmasi.lower() == "ya":
            nama = input ("\nNama pemesan : ")
            while nama == "":
                print("harap masukkan nama...")
                nama =input("Nama pemesan: ")

            while True:
                try:
                    jumlah = input("Pesen berapa tiket: ")
                    
                    if jumlah == "":
                        print("Harap masukkan jumlah tiket.")
                        continue 
                    jumlah = int(jumlah)
                    break  

                except ValueError:
                    print("Input tidak valid! Harap masukkan angka yang benar untuk jumlah tiket.")

            tanggal = str(input("Tanggal wisata (format: DD-MM-YYYY): "))
            while tanggal == "":
                print("harap masukkan tanggal...")
                tanggal = input("Tanggal wisata (format: DD-MM-YYYY): ")
                break

            date['nama'] = nama
            date['tanggal'] = tanggal
            data_pembelian['jumlah'] = jumlah

            if jumlah > stok_paket["3"]:
                data_pembelian['jumlah3'] 
            elif jumlah <= stok_paket['3']:
                data_pembelian['jumlah3'] += jumlah
            
            if stok_paket["3"] < jumlah:
                print("\nMaaf Stok tidak mencukupi, stok yang tersedia:", stok_paket["3"])
                break

            stok_paket["3"] -= jumlah

            hasil = jumlah * 300000 
            data_pembelian['untung3'] += hasil
            data_pembelian['untung'] += hasil

            if jumlah > 20 :
                diskon = 10
                hitung_diskon = hasil * diskon // 100
                mendapat_diskon = hasil - hitung_diskon
                data_pembelian['untung3'] = mendapat_diskon
                data_pembelian['untung'] = mendapat_diskon
                print("Harga sebelum diskon: ",hasil)
                print("Harga sesudah diskon: ", mendapat_diskon, "mendapatkan dison sebesar",diskon,"%!!")
            else :
                print("Total yang harus dibayar : ",hasil)

            card()
            break
        elif konfirmasi != "tidak":
            print("inputkan yang benar")
        else:
            print("\nSilahkan Pilih paket yang lain")
            break
          
def card():
    for i in range(1):
        print("\n================ CARD UTM PARK ===============")
        print(f"\nnama pemesan            :{date['nama']}")
        print(f"pesan paket             :{kumpulan_paket[0]}")
        print(f"jumlah pemesanan Tiket  :{data_pembelian['jumlah']}")
        print(f"Total Bayar             :{data_pembelian['untung']}")
        print(f"Tanggal Booking Tiket   :{date['tanggal']}")
        print("\nTerimakasih sudah memesan :)")
        print("#Tunjukkan ke kasir untuk mendapatkan kartu")

        print("\n=============================================")
        break

    
def menu():
    daftar()
    login()
    while True:
        print("\n=== DAFTAR PAKET TIKET MASUK WISATA UTM PARK ===")
        print("1. Paket 1 : Animals Park")
        print("2. Paket 2 : Wahana Asik Asikan, Zona Berenang" )
        print("3. Paket 3 : Animals Park , Wahana Asik Asikan, Zona Berenang")   
        print("4. Keluar")   
        paket = input("\nPilih Mau ambil Paket yang mana :")
        if paket == "1":
            kumpulan_paket.append(paket) 
            paket_satu()
            kumpulan_paket.pop(0)        
        elif paket == "2":
            kumpulan_paket.append(paket)
            paket_dua() 
            kumpulan_paket.pop(0) 
        elif paket == "3":
            kumpulan_paket.append(paket)
            paket_tiga() 
            kumpulan_paket.pop(0) 
        elif paket == "4":
            print("Terimakasih Telah Mengakses Dengan menggunakan program ini")
            break
        else: 
            print("Inputkan yang benar, contoh 1/2/3/4")


   


def login_karyawan():
    while True:
        nip = {'kafi':240441100035,'dhani':240441100079}
        print("\nPROGRAM HANYA BISA DIAKSES DENGAN NOMOR NIP")
        while True:
            try:
                no_nip =int(input("\nmasukkan nomor NIP anda : "))
                    
                if no_nip == "":
                    print("Harap masukkan nip anda...")
                    continue 
                no_nip = int(no_nip)
                break  

            except ValueError:
                print("Input tidak valid! Harap masukkan nip yang benar untuk login...")

        if no_nip != nip['kafi'] and no_nip != nip['dhani']:
            print("Nomor NIP anda salah")
        else:
            print("\nAnda berhasil login !")
            break
def menu_karyawan ():
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Cek data tiket yang terjual ")
        print("2. Cek keuntungan")
        print("3. Cek stok paket")
        print("4. Keluar")
        

        cek = input("pilih (1/2/3/4): ")

        if cek == "1":
            while True:
                print("\n== MENU DATA TIKET YANG TERJUAL ==")
                print("1.Cek data tiket paket 1")
                print("2.Cek data tiket paket 2")
                print("3.Cek data tiket paket 3")
                print("4.Cek Seluruh Data")
                print("5.Keluar")

                cek_lagi = input("(1/2/3/4/5): ")
                if cek_lagi == "1":
                    print(f"\ndata tiket paket 1 yang terjual : {data_pembelian['jumlah1']} Tiket")
                elif cek_lagi == "2":
                    print(f"\ndata tiket paket 2 yang terjual : {data_pembelian['jumlah2']} Tiket")
                elif cek_lagi == "3":
                    print(f"\ndata tiket paket 3 yang terjual : {data_pembelian['jumlah3']} Tiket")
                elif cek_lagi == "4":
                    print(f"\nTotal seluruh tiket yang terjual : {data_pembelian['jumlah1'] + data_pembelian['jumlah2'] + data_pembelian['jumlah3']} Tiket") 
                elif cek_lagi == "5":
                    break
                else:
                    print("inputan tidak valid")
        elif cek == "2":
            while True:
                print("\n== MENU DATA KEUNTUNGAN TIKET == ")
                print("\n1.Cek keuntungan Paket 1")
                print("2.Cek keuntungan Paket 2")
                print("3.Cek keuntungan Paket 3")
                print("4.Cek Keuntungan Semua Paket")
                print("5.Keluar")
                cek_lagi = input("(1/2/3/4/5) : ")
                if cek_lagi == "1":
                    print(f"\nKeuntungan Penjualan Dari Paket 1: Rp.{data_pembelian['untung1']}")
                elif cek_lagi == "2":
                    print(f"\nKeuntungan Penjualan Dari Paket 2: Rp.{data_pembelian['untung2']}")
                elif cek_lagi == "3":
                    print(f"\nKeuntungan Penjualan Dari Paket 3: Rp.{data_pembelian['untung3']}")
                elif cek_lagi == "4":
                    print(f"\nTotal Keuntungan yang di dapat : Rp.{data_pembelian['untung1'] + data_pembelian['untung2'] + data_pembelian['untung3']}") 
                elif cek_lagi == "5":
                    break
                else:
                    print("inputan tidak valid")
        elif cek == "3":
            print("\n== MENU DATA STOK PAKET ==")
            print("\nStok Paket Tersedia:")
            for paket, stok in stok_paket.items():
                print(f"PAKET {paket}: {stok} tiket")

        elif cek == "4":
            print("Terimakasih Telah Mengakses Program ini")
            break
        else:
            print("Mohon masukkan angka(1/2/3/4)")

menu()
login_karyawan()
menu_karyawan()