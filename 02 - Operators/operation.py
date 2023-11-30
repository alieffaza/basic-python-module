print("==========================") #Menampilkan string yang berbentuk seperti garis
print("| Program Python Modul 2 |") #Menampilkan string berupa judul program
print("==========================") #Menampilkan string yang berbentuk seperti garis

print("==| Operator Artimatika |==") #Menampilkan string berupa judul operator
x = int(input("Masukan Nilai x = ")) #Membuat input untuk user memasukan nilai variabel x
y = int(input("Masukan Nilai y = ")) #Membuat input untuk user memasukan nilai variabel y
print("==========================")  #Menampilkan string yang berbentuk seperti garis
print("x + y  =", x + y)  #Menampilkan hasil dari operasi penjumlahan nilai x dan y
print("x - y  =", x - y)  #Menampilkan hasil dari operasi pengurangan nilai x dan y
print("x * y  =", x * y)  #Menampilkan hasil dari operasi perkalian nilai x dan y
print("x / y  =", x / y)  #Menampilkan hasil dari operasi pembagian nilai x dan y
print("x % y  =", x % y)  #Menampilkan hasil dari operasi modulus sisa bagi dari nilai x dan y
print("x ** y =", x ** y) #Menampilkan hasil dari operasi pemangkatan nilai x dan y
print("x // y =", x // y) #Menampilkan hasil dari operasi pembagian nilai x dan y dan hasilnya bilangan bulat
print("==========================") #Menampilkan string yang berbentuk seperti garis

print("==| Operator Assignment |==") #Menampilkan string berupa judul operator
x = int(input("Masukan Nilai x = ")) #Membuat input untuk user memasukan nilai variabel x
print("==========================")  #Menampilkan string yang berbentuk seperti garis
x += 5 #Melakukan operasi penjumlahan nilai x dengan 5
print("Hasil x += 5  adalah", x) #Menampilkan hasil dari operasi penjumlahan nilai x dengan 5
x -= 3 #Melakukan operasi pengurangan nilai x dengan 3
print("Hasil x -= 3  adalah", x) #Menampilkan hasil dari operasi pengurangan nilai x dengan 3
x *= 4 #Melakukan operasi perkalian nilai x dengan 4
print("Hasil x *= 4  adalah", x) #Menampilkan hasil dari operasi perkalian nilai x dengan 4
x /= 2 #Melakukan operasi pembagian nilai x dengan 2
print("Hasil x /= 2  adalah", x) #Menampilkan hasil dari operasi pembagian nilai x dengan 2
x **= 2 #Melakukan operasi pemangkatan nilai x dengan 2
print("Hasil x **= 2 adalah", x) #Menampilkan hasil dari operasi pemangkatan nilai x dengan 2
x //= 3 #Melakukan operasi pembagian nilai x dengan 3
print("Hasil x //= 3 adalah", x) #Menampilkan hasil dari operasi pembagian nilai x dengan 3
x %= 2 #Melakukan operasi modulus sisa bagi nilai x dengan 2
print("Hasil x %= 2  adalah", x) #Menampilkan hasil dari operasi modulus sisa bagi nilai x dengan 2
print("==========================") #Menampilkan string yang berbentuk seperti garis

print("==| Operator Perbandingan |==") #Menampilkan string berupa judul operator
x = 5  #Variabel nilai x
y = 7  #Variabel nilai y
x == y #Membandingkan apakah nilai x dan nilai y bernilai sama
x != y #Membandingkan apakah nilai x dan nilai y bernilai tidak sama
x > y  #Membandingkan apakah nilai x lebih besar dari nilai y 
x < y  #Membandingkan apakah nilai x lebih kecil dari nilai y
x >= y #Membandingkan apakah nilai x lebih besar atau sama dengan nilai y
x <= y #Membandingkan apakah nilai x lebih kecil atau sama dengan nilai y

print("==| Operator Logika |==") #Menampilkan string berupa judul operator
x = 7 #Variabel nilai x
x < 5 and x < 10 #Menggunakan gerbang logika AND untuk melihat apakah inputan menghasilkan nilai true atau false
x < 5 or x < 10  #Menggunakan gerbang logika OR untuk melihat apakah inputan menghasilkan nilai true atau false
not x > 10 and x < 50 #Menggunakan gerbang logika NAND untuk melihat apakah inputan menghasilkan nilai true atau false (hasilnya inverse/terbalik)

print("==| Operator Identitas |==") #Menampilkan string berupa judul operator
x = 5 #Variabel nilai x
y = 5 #Variabel nilai y
x is y #Memastikan apakah nilai x dan y identik/sama
x is not y #Memastikan apakah nilai x dan y tidak identik/tidak sama

print("==| Operator Keanggotaan |==") #Menampilkan string berupa judul operator
x = "Alief Faza Rizqi Adi Jaya" #Membuat variabel dengan tipe data string
"a" in x #Memastikan apakah huruf tersebut termasuk sebagai anggota dalam string tersebut
"s" not in x #Memastikan apakah huruf tersebut tidak termasuk sebagai anggota dalam string tersebut


print("==| Operator Bitwise |==") #Menampilkan string berupa judul operator
x = 4 #Variabel nilai x
y = 6 #Variabel nilai y
x & y #Menggunakan gerbang logika AND pada nilai x dan nilai y kedalam angka biner
x | y #Menggunakan gerbang logika OR pada nilai x dan nilai y kedalam angka biner
y ^ y #Menggunakan gerbang logika XOR pada nilai x dan nilai y kedalam angka biner
x << y #Melakukan Left shift pada nilai x dan nilai y kedalam angka biner
x >> y #Melakukan Right shift  pada nilai x dan nilai y kedalam angka biner