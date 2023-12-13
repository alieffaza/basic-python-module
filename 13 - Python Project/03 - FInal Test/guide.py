# Import untuk menggunakan kode dari modul TKinter
import tkinter as tk # tk adalah as(alias) supaya modul lebih singkat & mudah digunakan

# Import untuk menggunakan kode messagebox dari Module Tkinter
from tkinter import messagebox # messagebox berfungsi untuk menampilkan kotak peringatan

# Buat Kelas untuk PBO (Pemrograman Berorientasi Objek)
class Kontak: # Kelas Kontak fungsinya untuk menyimpan informasi kontak

    # Buat konstruktor dengan parameter self, nama, no_telp, email, deskripsi
    def __init__(self, nama, no_telp, email, deskripsi): # init untuk inialisasi objek

        # Buat instance objek
        self.nama = nama # Self merujuk pada objek itu sendiri. self.nama untuk menyimpan data nama
        self.no_telp = no_telp # Self merujuk pada objek itu sendiri. self.no telp untuk menyimpan data no telp
        self.email = email # Self merujuk pada objek itu sendiri. self.email untuk menyimpan data email
        self.deskripsi = deskripsi # Self merujuk pada objek itu sendiri. self.deskripsi untuk menyimpan data deskripsi

# Kelas KontakApp untuk membuat antarmuka/tampilan aplikasi
class KontakApp:

    # Buat konstruktor dengan parameter self, root
    def __init__(self, root): # init untuk inialisasi objek

        # Inisialisasi root Aplikasi
        self.root = root # root adalah elemen utama dasar(default) dari modul tkinter

        # Judul Aplikasi
        self.root.title("Aplikasi Kontak") # root.title untuk membuat judul aplikasi

        # Buat listkontak untuk menyimpan data kontak
        self.listkontak = [] # List kosong untuk menampung data yang nanti dimasukan

        # Buat antarmuka Aplikasi
        self.create_widgets() #create_widget untuk membuat tampilan dari modul tkinter

    # Buat antarmuka Aplikasi
    def create_widgets(self): # self digunakan untuk akses atribut objek
        
        # Buat label untuk input data kontak
        labels = ["Nama:", "No. Telepon:", "Email:", "Deskripsi:"] # label untuk kotak 
        
        # Buat perulangan label untuk label_text berarti mengulang 4 label
        for i, label_text in enumerate(labels): # enumerate untuk memasangkan nilai index dengan label
            
            # Tampilkan label pada Aplikasi
            tk.Label(self.root, text=label_text).grid(row=i, column=0)  # tk.label elemen untuk membuat label dari tkinter
                                                                        # grid untuk posisi
                                                                        # row untuk posisi baris dan i berarti sesuai index labelnya
                                                                        # column untuk posisi kolom, 0 berarti di index 0

        # Buat field entry untuk kotak input
        self.entry_fields = [tk.Entry(self.root) for _ in range(len(labels))] # self.entry_fields list berisi objek dari tk.entry
                                                                              # tk.entry adalah label untuk kotak input dari modul tkinter
                                                                              # range(len(labels)) untuk menghasilkan urutan angka sesuai dengan elemen dalam label
                                                                              # _ untuk melakukan perulangan tanpa melihat urutan indexnya


        # Buat perulangan untuk memasukan data
        for i, entry in enumerate(self.entry_fields): #untuk mengakses nilai dan indeks dari kotak

            # Tampilkan data masukan pada Aplikasi
            entry.grid(row=i, column=1) # grid untuk posisi
                                        # row untuk posisi baris dan i berarti sesuai index kotaknya
                                        # column untuk posisi kolom, 1 berarti di index 1

        # Buat tombol untuk aksi
        button_texts = ["Tambah Kontak", "Hapus Kontak", "Simpan ke File"] # list untuk tombol yang akan ditampilkan 

        # Beri perintah untuk tombol tersebut
        perintah = [self.add_kontak, self.delete_kontak, self.Print] # llst perintah untuk alamat fungsi dari tombol tersebut

        # Buat perulangan untuk tombol
        for i, (text, command) in enumerate(zip(button_texts, perintah), start=len(labels)):

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
            messagebox.showinfo("Pemberitahuan", "Data berhasil ditambahkan!") 
        
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
            messagebox.showinfo("Pemberitahuan", "Data berhasil dihapus!") 

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
        with open("kontak-saya.txt", "w") as file:
        
            # Buat perulangan jika ada kontak baru
            for kontak in self.listkontak:
        
                # Tulis informasi kontak ke dalam file teks
                file.write(f"{kontak.nama}, {kontak.no_telp}, {kontak.email}, {kontak.deskripsi}\n")
            
            messagebox.showinfo("Pemberitahuan", "Data berhasil disimpan ke kontak-saya.txt!") 

# Cek Module tersebut
if __name__ == "__main__":

    # Inisialisasi Aplikasi utama
    root = tk.Tk()  

    # Buat objek KontakApp
    app = KontakApp(root)  

    # Mulai perulangan untuk aplikasi
    root.mainloop()  