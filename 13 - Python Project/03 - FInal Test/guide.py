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
                                                                        # grid untuk posisi label
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
        for i, (text, command) in enumerate(zip(button_texts, perintah), start=len(labels)): # for i untuk 
                                                                                             # len untuk memberi nomor index pada 
                                                                                             # zip untuk menggabungkan nilai dari list button dan perintah
                                                                                             # enumerate untuk mengurutkan index dalam perulangan

            # Tampilkan tombol masukan pada Aplikasi
            tk.Button(self.root, text=text, command=command).grid(row=i, column=0, columnspan=2, pady=5) # tk.button untuk membuat tombol dengan kode dari modul tkinter
                                                                                                         # row untuk posisi baris dan i berarti sesuai index labelnya
                                                                                                         # column untuk posisi kolom, 0 berarti di index 0
                                                                                                         # columspan untuk jarak antara teks dan kotak tombol
                                                                                                         # pady untuk jadi untuk jarak antar tombol 

        # Buat Listbox untuk menampilkan daftar kontak
        self.kontak_listbox = tk.Listbox(self.root, width=50) # self.kontak_listbox untuk membuat sebuah kotak berisi list
                                                              # tk.listbox fungsi dari modul tk inter untuk membuat listbox
                                                              # width untuk ukuran dari listbox

        # Tampilkan daftar kontak
        self.kontak_listbox.grid(row=0, column=2, rowspan=len(labels)) # self.kontak_listbox.grid untuk membuat ukuran dari listbox
                                                                       # row untuk posisi baris dan 0 berarti ada pada index 0
                                                                       # column untuk posisi kolom, 2 berarti di index 2
                                                                       # rowspan jarak antara teks dan kotak listbox, ukurannya len(labels) berarti menyesuaikan ukuran dari data pada label

    # Method untuk menambahkan kontak baru
    def add_kontak(self): # membuat fungsi untuk menambahkan data

        # Ambil nilai dari field entry
        values = [entry.get() for entry in self.entry_fields] # list values berisi data dari entryfield
                                                              # entry get adalah method untuk mengambil data dari entrylist

        # Jika semua field terisi, maka:
        if all(values): # struktur kondisi jika semua value terpenuhi, maka
                        # all untuk mengecek apakah semua value bernilai true(diisi)

            # Buat objek Kontak baru
            kontak = Kontak(*values) # *values untuk membongkat nilai value dan memngirimnya sebagai argumen ke konstruktor
            
            # Tambahkan objek baru ke daftar kontak
            self.listkontak.append(kontak) # append untuk menambahkan data
            
            # Update tampilan list kontak
            self.update_kontak_listbox() # update untuk merubah tampilan saat ada data baru
            
            # Kosongkan field entry
            self.clear_entry_fields() # clear untuk mengosongkan kotak entry jika data sudah ditambahkan 

            # buat sebuah pemberitahuan 
            messagebox.showinfo("Pemberitahuan", "Data berhasil ditambahkan!") # showinfo untuk menampilkan pemberitahuan jika data berhasil ditambahkan
        
        # Jika field kosong, maka:
        else:
            
            # Tampilkan peringatan field kosong
            messagebox.showwarning("Peringatan", "Semua kolom harus diisi!") # showwarning untuk menampikan pemberitahuan gagal

    # Buat Method untuk menghapus kontak yang dipilih
    def delete_kontak(self): # membuat fungsi untuk menhapus kontak
        
        # Ambil data indeks kontak yang dipilih
        selected_index = self.kontak_listbox.curselection() # curselection untuk memilih index dari data yang dipilih kursor
        
        # Jika kontak sudah dipilih, maka:
        if selected_index: 
            
            # Hapus kontak dari daftar
            del self.listkontak[selected_index[0]] # menghapus data yang dipilih berdasarkan index
                                                   # 0 untuk mengakses indeks pertama dari item yang dipilih
            
            # Update tampilan list kontak
            self.update_kontak_listbox()  # update untuk memperbarui data yang sudah terhapus

            # Tampilkan pemberitahuan
            messagebox.showinfo("Pemberitahuan", "Data berhasil dihapus!") # showinfo untuk menampilkan pemberitahuan jika data berhasil ditambahkan

    # Buat Method untuk perbarui tampilan list kontak
    def update_kontak_listbox(self): # membuat fungsi untuk update listbox
        
        # Hapus semua item pada listbox
        self.kontak_listbox.delete(0, tk.END) # delete untuk hapus data
                                              # 0 untuk memilih index pertama dari item yang dipilih
                                              # tk.end untuk menunjukan index akhir dari item yang dipilih
        
        # Buat perulangan untuk memasukan data lagi
        for kontak in self.listkontak: # perulangan untuk menambah data baru
            
            # Tambahkan informasi kontak ke dalam listbox
            self.kontak_listbox.insert(tk.END, f"{kontak.nama} - {kontak.no_telp} - {kontak.email} - {kontak.deskripsi}") # tampilkan data nama, telp , email, deskripsi
                                                                                                                          # menggunakan formating string

    # Buat Method untuk mengosongkan field entry
    def clear_entry_fields(self): # buat fungsi kosongkan entry field 
        
        # Buat perulangan untuk memasukan data lagi
        for entry in self.entry_fields: # pengulangan dari masing masing data dalam entry field 
            
            # Hapus semua nilai pada field entry
            entry.delete(0, tk.END) # delete untuk menghapus nilai pada entry fields
                                    # 0 dan tk.end berarti memilih indeks 0 sampai indeks terakhir

    # Buat Method untuk mencetak kontak ke dalam file txt
    def Print(self): # membuat fungsi untuk print ke file
        
        # Buka/buat file aplikasi-kontak.txt
        with open("kontak-saya.txt", "w") as file: # open as file untuk membuka file "kontak-saya.txt"
                                                   # "w" (write) untuk menulis 
        
            # Buat perulangan sesuai nilai data kontak
            for kontak in self.listkontak: 
        
                # Tulis informasi kontak ke dalam file teks
                file.write(f"{kontak.nama}, {kontak.no_telp}, {kontak.email}, {kontak.deskripsi}\n") # f untuk string formatting
                                                                                                     # {} untuk mengambil data 
                                                                                                     # \n untuk memberi jarak
            
            messagebox.showinfo("Pemberitahuan", "Data berhasil disimpan ke kontak-saya.txt!") 

# Cek Module tersebut
if __name__ == "__main__":

    # Inisialisasi Aplikasi utama
    root = tk.Tk()  

    # Buat objek KontakApp
    app = KontakApp(root)  

    # Mulai perulangan untuk aplikasi
    root.mainloop()  