mahasiswa = {
    'nama':"Alief Faza Rizqi Adi Jaya",
    'prodi':"Teknik Informatika",
    'nim':2311102441109,
    'angkatan':2023
    }

print("\n Mengakses data Nama:", mahasiswa['nama'])

print("\n Mengecek index data Dictionary:")
for index, key in enumerate(mahasiswa):
    print(f'Index:{index}, Kunci:{key}')
