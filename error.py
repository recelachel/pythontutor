print("KALKULATOR SEDERHANA")
try:
    angka1 = int(input("Angka pertama : "))
    angka2 = int(input("Angka kedua : "))
    hasil = angka1/angka2
    print("Hasil : ", hasil)
except:
    print("Terjadi error dalam perhitungan!")