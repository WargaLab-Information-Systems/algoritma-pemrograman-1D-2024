def kelola_klub_ekstrakurikuler(klub_basket, klub_renang):
    hasil = {
        "siswa_kedua_klub": klub_basket .intersection(klub_renang),  
        "siswa_satu_klub": klub_basket  .symmetric_difference(klub_renang),  
        "semua_siswa_unik": klub_basket .union(klub_renang),  
    }
    hasil["jumlah_siswa_unik"] = len(hasil["semua_siswa_unik"])

    print("Siswa yang mengikuti kedua klub:", hasil["siswa_kedua_klub"])
    print("Siswa yang hanya mengikuti satu klub:", hasil["siswa_satu_klub"])
    print("Semua siswa unik:", hasil["semua_siswa_unik"])
    print("Jumlah siswa unik:", hasil["jumlah_siswa_unik"])

    return hasil
klub_basket = {"salman","dhani","sheva","ajez","awung","adit"}
klub_renang = {"jainal","salman","dhani","awung"}

kelola_klub_ekstrakurikuler(klub_basket, klub_renang)

