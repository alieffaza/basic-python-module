mahasiswa = {
    'nama':"Alief Faza Rizqi Adi Jaya",
    'prodi':"Teknik Informatika",
    'nim':2311102441109,
    'angkatan':2023
    }

print("\n Perulangan pada index:")
for index, key in enumerate(mahasiswa):
    print(f'Index:{index}, Kunci:{key}')
    
print("\n Akses index pada perulangan:")
for key in mahasiswa:
    value = mahasiswa[key]
    print(f'Kunci:{key}, Nilai:{value}')

print("\n Perulangan pada Value:")
for value in mahasiswa.values():
    print(f'Nilai: {value}')

print("\n Perulangan pada Item:")
for key, value in mahasiswa.items():
    print(f'Kunci:{key}, Nilai: {value}')
