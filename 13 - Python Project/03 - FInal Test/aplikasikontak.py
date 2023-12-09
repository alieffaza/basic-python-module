# Import modul TKinter
import tkinter as tk
# Import messagebox dari Module Tkinter
from tkinter import messagebox

# Buat class Kontak untuk menyimpan informasi kontak
class Kontak:
    # Buat konstruktor untuk Inialisasi Objek dengan atribut self, nama, no telp, email, deskripsi
    def __init__(self, nama, no_telp, email, deskripsi):
        # Buat instance dari atribut class Kontak
        self.nama = nama
        self.no_telp = no_telp
        self.email = email
        self.deskripsi = deskripsi

# Buat class KontakApp untuk antarmuka/tampilan aplikasi
class KontakApp:
    # Buat konstruktor untuk Inialisasi Objek dengan atribut self, root
    def __init__(self, root):
        # Inisialisasi root Aplikasi
        self.root = root
        # Judul Aplikasi
        self.root.title("Aplikasi Kontak") 

        # Buat List untuk menyimpan data kontak
        self.listkontak = []

        # Buat antarmuka Aplikasi
        self.create_widgets()

    # Buat antarmuka Aplikasi
    def create_widgets(self):
        # Buat label untuk input data kontak
        labels = ["Nama:", "No. Telepon:", "Email:", "Deskripsi:"]
        #Buat perulangan untuk label
        for i, label_text in enumerate(labels):
            # Tampilkan label pada Aplikasi
            tk.Label(self.root, text=label_text).grid(row=i, column=0)  

        # Buat field entry untuk input data
        self.entry_fields = [tk.Entry(self.root) for _ in range(len(labels))]
        # Buat perulangan untuk memasukan data
        for i, entry in enumerate(self.entry_fields):
            # Tampilkan data masukan pada Aplikasi
            entry.grid(row=i, column=1)  

        # Buat tombol untuk aksi
        button_texts = ["Tambah Kontak", "Hapus Kontak", "Simpan ke File"]
        # Beri perintah untuk tombol tersebut
        commands = [self.add_kontak, self.delete_kontak, self.Print]  

        # Buat perulangan untuk tombol
        for i, (text, command) in enumerate(zip(button_texts, commands), start=len(labels)):
            # Tampilkan tombol masukan pada Aplikasi
            tk.Button(self.root, text=text, command=command).grid(row=i, column=0, columnspan=2, pady=5)  

        # Buat Listbox untuk menampilkan daftar kontak
        self.kontak_listbox = tk.Listbox(self.root, width=50)
        # Tampilkan daftar kontak
        self.kontak_listbox.grid(row=0, column=2, rowspan=len(labels)) 

    # Method untuk menambahkan kontak baru
    def add_kontak(self):
        # Ambil nilai dari field entry
        values = [entry.get() for entry in self.entry_fields]  
        # Jika semua field terisi, maka:
        if all(values):  
            # Buat objek Kontak baru
            kontak = Kontak(*values)  
            # Tambahkan ke daftar kontak
            self.listkontak.append(kontak)  
            # Update tampilan list kontak
            self.update_kontak_listbox()  
            # Kosongkan field entry
            self.clear_entry_fields()  
        # Jika field kosong, maka:
        else:
            # Tampilkan peringatan field kosong
            messagebox.showwarning("Peringatan", "Semua kolom harus diisi!")  

    # Buat Method untuk menghapus kontak yang dipilih
    def delete_kontak(self):
        # Ambil data indeks kontak yang dipilih
        selected_index = self.kontak_listbox.curselection()  
        # Jika kontak sudah dipilih, maka:
        if selected_index:
            # Hapus kontak dari daftar
            del self.listkontak[selected_index[0]]  
            # Update tampilan list kontak
            self.update_kontak_listbox()  

    # Buat Method untuk perbarui tampilan list kontak
    def update_kontak_listbox(self):
        # Hapus semua item pada listbox
        self.kontak_listbox.delete(0, tk.END)  
        # Buat perulangan untuk memasukan data lagi
        for kontak in self.listkontak:
            # Tambahkan informasi kontak ke dalam listbox
            self.kontak_listbox.insert(tk.END, f"{kontak.nama} - {kontak.no_telp} - {kontak.email} - {kontak.deskripsi}")

    # Buat Method untuk mengosongkan field entry
    def clear_entry_fields(self):
        # Buat perulangan untuk memasukan data lagi
        for entry in self.entry_fields:
            # Hapus semua nilai pada field entry
            entry.delete(0, tk.END)  

    # Buat Method untuk mencetak kontak ke dalam file txt
    def Print(self):
        # Buka/buat file aplikasi-kontak.txt
        with open("aplikasi-kontak.txt", "w") as file:
            # Buat perulangan jika ada kontak baru
            for kontak in self.listkontak:
                # Tulis informasi kontak ke dalam file teks
                file.write(f"{kontak.nama}, {kontak.no_telp}, {kontak.email}, {kontak.deskripsi}\n")

# Cek Module tersebut
if __name__ == "__main__":
    # Inisialisasi Aplikasi utama
    root = tk.Tk()  
    # Buat objek KontakApp
    app = KontakApp(root)  
    # Mulai perulangan untuk aplikasi
    root.mainloop()  