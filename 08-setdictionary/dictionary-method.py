bio = {
    'nama':"Alief Faza Rizqi Adi Jaya",
    'nim':2311102441109
}

#Method get
print("Nilai nim dari Dictionary tersebut:", bio.get('nim'))

#Method items
print("Item pada Dictionary tersebut:", bio.items())

#Method fromkeys
keys = ['nama', 'nim']
value = "Alief Faza Rizqi Adi Jaya", 2311102441109
dict_fromkeys = dict.fromkeys(keys,value)
print("Dictionary hasil Fromkeys:", dict_fromkeys)