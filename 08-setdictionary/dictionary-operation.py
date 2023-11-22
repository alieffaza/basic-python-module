mahasiswa = {
    'nama':"Alief Faza Rizqi Adi Jaya",
    'prodi':"Teknik Informatika",
    'nim':2311102441109,
    'angkatan':2023
    }

print("\n Mengakses data Nama:", mahasiswa['nama'])

print("\n Mengecek value dari sebuah kunci:")
for key in mahasiswa:
    value = mahasiswa[key]
    print(f'Kunci:{key}, Nilai:{value}')