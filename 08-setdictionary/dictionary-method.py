mahasiswa = {
    'nama':"Alief Faza Rizqi Adi Jaya",
    'nim':2311102441109
}
print("\n", mahasiswa)

#Method get
print("\n Nilai nim dari Dictionary tersebut:", mahasiswa.get('nim'))

#Method values
values = mahasiswa.values()
print("\n Nilai dari Dictionary tersebut:", values)

#Method keys
keys =  mahasiswa.keys()
print("\n Kunci dari Dictionary tersebut:", keys)

#Method copy
copy_mahasiswa = mahasiswa.copy()
print("\n Copy dari Dictionary tersebut:", copy_mahasiswa)

#Method update 
update = mahasiswa.update({'prodi':'S1 Teknik Informatika'})
print("\n Mengupdate data baru kedalam Dictionary tersebut:", update)

#Method setdefault
setdefault = mahasiswa.setdefault('nim')
print("\n Data dari kunci nim pada Dictionary tersebut:", setdefault)

#Method items
print("\n Item pada Dictionary tersebut:", mahasiswa.items())

#Method fromkeys
keys = ['nama', 'nim']
value = "Alief Faza Rizqi Adi Jaya", 2311102441109
dict_fromkeys = dict.fromkeys(keys,value)
print("\n Dictionary hasil Fromkeys:", dict_fromkeys)

#Method pop
pop = mahasiswa.pop('nim')
print("\n Menghapus data nim pada Dictionary tersebut:", pop)

#Method clear
clear = mahasiswa.clear()
print("\n Menghapus semua data pada Dictionary tersebut:", clear)