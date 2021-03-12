print ("====Identitas Pribadi====")
nama_lengkap = "Audrey Alexandra"
nama_panggilan = "Audrey"
jenis_kelamin = "perempuan"
tempat_lahir = "Jakarta"
alamat = "Pondok Kopi vb F8 No 2"
umur = 18
tanggal_lahir = 18
bulan_lahir = 11
tahun_lahir = 2002
lahir = tahun_lahir + (bulan_lahir*30) + (tahun_lahir*365)

tanggalsekarang = 12
bulansekarang = 3
tahunsekarang = 2021
sekarang = tahunsekarang + (bulansekarang*30) + (tahunsekarang*365)

tahun = int((sekarang - lahir) / 365)
bulan = int(((sekarang - lahir)%365) / 30)
hari = int(((sekarang - lahir)%365) % 30)

bulann = (tahun*12) + bulan

gol_darah = "O"
ukuran_sepatu = 23.5
tinggi_badan = 158
warna_favorit = "hitam"
hobi = "nonton film"
makanan_favorit = "cumi goreng tepung"
minuman_favorit = "lemon tea"
status = "Belum Menikah"
nama_ayah = "Roganda Siregar"
nama_ibu = "Herlina Simbolon"
nama_abang = "Galvani"
pekerjaan = "mahasiswa"
universitas = "Universitas Sebelas Maret"
jurusan = "Teknik Industri"
angkatan = 2020

print("=================================================")
print(" ==================== Identitas Diri ==================")
print("=================================================")
print ("")
print("Haii!!!")
print ("Perkenalkan namaku",nama_lengkap,", orang-orang biasa memanggilku dengan",nama_panggilan,"jenis kelaminku adalah",jenis_kelamin,". Aku berumur" ,umur,"tahun, perempuan kelahiran",tempat_lahir,", pada tanggal",tanggal_lahir,"bulan",bulan_lahir,"tahun",tahun_lahir,"aku Bergolongan darah",gol_darah,"golongan darah yang paling mudah mendapatkan pendonor.")
print("Aku tinggal di",alamat,",bersama kedua orang tuaku dan abang, ayahku",nama_ayah,"dan ibuku",nama_ibu," dan abangku",nama_abang,)
print("Aku memiliki tinggi",tinggi_badan,"mungkin anak yang paling tinggi di kelas heheh,. Oh ya  bagi yag ingin tau ukuran sepatuku",ukuran_sepatu,"cm hehehe.")
print("Makanan Kesukaanku adalah",makanan_favorit,"Minuman kesukaanku",minuman_favorit,"warna kesukaanku adalah",warna_favorit,"Salah satu hobiku adalah",hobi,"dan masih banyak lagi.")
print("sekarang aku adalah",pekerjaan,"di salah satu universitas ternama di Indonesia yaitu",universitas,"dengan jurusan",jurusan,"angkatan",angkatan,"cukup sampai disini perkenalan diriku  See you :)")
print("==========================================================")







