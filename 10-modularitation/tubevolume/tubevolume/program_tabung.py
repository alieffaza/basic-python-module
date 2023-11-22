import module_tabung

def main():
    r = float(input(f"\n Masukan jari jari lingkaran : "))
    t = float(input(f"\n Masukan tinggi tabung : "))
    volume = module_tabung.volume_tabung(r, t)
    print(f"\n Jari jari lingkaran: {r} \n Tinggi tabung : {t} \n Volume tabung : {volume}")

if __name__ == "__main__":
    main()