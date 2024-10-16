#seleksi pendaftaran beasiswa dengan ketentuan:
skor_minimal = 1100
ipk_minimal = 3.0
# data mahasiswa :
jaka_skor = 1100
jaka_ipk = 3.5

ida_skor = 1000
ida_ipk = 3.5
# mengecek persyaratan beasiswa jaka, seleksi kondisi
if jaka_skor >= 1100 and jaka_ipk > 3.0 :
    print
    print ("selamat anda lolos persyaratan beasiswa untuk jaka")
else:
    print ("maaf anda tidak lolos persyaratan beasiswa untuk jaka")  
if ida_skor > 1100 and ida_ipk > 3.0 :
#mengecek persyaratan beasiswa ida
    
    print ("selamat anda lolos persyaratan beasiswa untuk ida") 
else:
    print ("maaf anda tidak lolos seleksi beasiswa untuk ida") 

  
