# Definisikan fungsi lambda untuk mengkuadratkan nilai angka
pangkatkan_angka = lambda angka: (angka ** 2)

# Definisikan fungsi lambda untuk cek apakah angka kurang dari atau sama dengan 5
cek_bilangan_genap = lambda angka: angka <= 5

# Definisikan fungsi lambda yang menampilkan sebuah string berisi nama
hello = lambda: ("Alief Faza Rizqi Adi Jaya")

# Cetak fungsi lambda hello 
print(hello)

# Cetak hasil dari fungsi pangkatkan_angka dengan argumen 5
print(pangkatkan_angka(5))

# Cetak hasil dari fungsi cek_bilangan_genap dengan argumen 7
print(cek_bilangan_genap(7))

# List berisi angka
angka_ajaib = [1, 2, 3, 4, 5, 6, 7, 8]

# pangkatkan setiap angka dalam angka_ajaib dan ubah menjadi list
print(list(map(lambda angka: (angka * 2), angka_ajaib)))

# Kuadratkan setiap angka dalam angka_ajaib dan ubah menjadi list
print(list(map(lambda angka: (angka ** 2), angka_ajaib)))

# Filter angka dalam 'angka_ajaib' yang kurang dari atau sama dengan 2 dan ubah menjadi list
print(list(filter(lambda angka: angka <= 2, angka_ajaib)))
