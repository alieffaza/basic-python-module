import module_arithmetic

def main():
    x = 2
    y = 4

    print("Nilai x :", x)
    print("Nilai y :", y)

    tambah = module_arithmetic.penjumlahan(x, y)
    print(f"Hasil Penjumlahan : {tambah}")

    kurang = module_arithmetic.pengurangan(x, y)
    print(f"Hasil Pengurangan : {kurang}")

    kali = module_arithmetic.perkalian(x, y)
    print(f"Hasil Perkalian : {kali}")

    bagi = module_arithmetic.pembagian(x, y)
    print(f"Hasil Pembagian : {bagi}")

    pangkat = module_arithmetic.pemangkatan(x, y)
    print(f"Hasil Pemangkatan : {pangkat}")

if __name__ == "__main__":
    main()