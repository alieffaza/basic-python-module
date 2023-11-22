gandakan_angka = lambda angka : (angka * 2)
pangkatkan_angka= lambda angka : (angka ** 2)
cek_bilangan_genap = lambda angka : angka <= 5
hello = lambda : ("Alief Faza Rizqi Adi Jaya")

print(hello)
print(gandakan_angka(5))
print(cek_bilangan_genap(7))

angka_ajaib = [1, 2, 3, 4, 5, 6, 7, 8]

print(list(map(lambda angka :(angka * 2), angka_ajaib)))
print(list(map(lambda angka :(angka ** 2), angka_ajaib)))
print(list(filter(lambda angka : angka <= 2, angka_ajaib)))