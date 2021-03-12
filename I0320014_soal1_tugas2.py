print("======== Program Menghitung Luas Persegi Panjang ========")
panjang=float(input(" Panjang: "))
lebar=float(input("Lebar: "))
luas=panjang*lebar
print("Luas persegi panjang adalah: ", luas, "satuan")

print("======== Program Menghitung Luas Lingkaran ========")
phi=3.14
r=float(input("Masukan Jari-Jari: "))
luas=phi*(r**2)
print("Luas lingkaran adalah: ", luas, "satuan")

print("======== Program Menghitung Luas Permukaan Kubus ========")
sisi=float(input("Masukan sisi: "))
luas_permukaan=6*(sisi**2)
print("Luas permukaan adalah: ", luas_permukaan, "Satuan")

print("======== Konversi Suhu Celcius ke Farenheit ========")
celcius=float(input("Masukan suhu dalam celcius: "))
fahrenheit=((9/5)*celcius)+32
print("Suhu: ", fahrenheit, "Fahrenheit")

print("======== Konversi Suhu Reamur ke Kelvin ========")
reamur=float(input("Masukan suhu dalam reamur: "))
kelvin=((5/4)*reamur)+273
print("Suhu: ", kelvin, "Kelvin")