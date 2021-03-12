#menampilkan informasi program

print("Konversi suhu (Faranheit ke Celcius)")

#input suhu dalam fahranheit
F= float(input("Masukkan suhu(fahranheit): "))

#melakukan konversi suhu ke celcius
C= 5 * (F-32) / 9

#menampilkan hasil konversi ke layar
print("Fahranheit: ", F)
print("Celcius:", C)