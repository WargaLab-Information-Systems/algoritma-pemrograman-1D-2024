while True:
    lama_minjam = int(input("Masukkan lama peminjaman maksimal 5 hari jika lebih akan terkena denda: "))
    total_denda = 0
    if lama_minjam > 5:
        denda_dibawah_10 = lama_minjam - 5
        total_denda = total_denda + denda_dibawah_10 * 2500 
         
    if lama_minjam > 10: 
        keterlambatan = denda_dibawah_10 - 10
        total_denda += (keterlambatan // 5) * 5500
                
    if total_denda > 0:
        print("total denda yang harus dibayar",total_denda)
    else:
        print(f"Anda meminjan selama {lama_minjam} hari jadi tidak terkena denda")
    
    konfirmasi_user = input("Apdakah Anda ingin menghitungnya lagi? [ya/tidak]")
    if konfirmasi_user != "ya":
        print("Terimakasih")
        break