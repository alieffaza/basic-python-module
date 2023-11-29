with open("12-document\\nnn.txt", "w") as file:
    file.writelines(f"\n Nama saya Faza \n dan umur ")

file = open("12-document\\nnn.txt", "r")
file_read = file.read()
print(file_read)