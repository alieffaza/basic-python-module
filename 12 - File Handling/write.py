file = open("12-document\\nnn.txt", "w")
file.write(f"Halo ini adalah file saya")

file = open("12-document\\nnn.txt", "r")
file_read = file.read()
print(file_read)