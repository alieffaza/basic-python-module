#Program Aritmatika
import module_arithmetic

def main():
    x = float(input("Masukan nilai x : "))
    y = float(input("Masukan nilai y : "))
    
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