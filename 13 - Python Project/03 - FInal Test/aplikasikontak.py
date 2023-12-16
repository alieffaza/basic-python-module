import tkinter as tk
from tkinter import messagebox 

class Kontak:
    def __init__(self, nama, no_telp, email, deskripsi):
        self.nama = nama 
        self.no_telp = no_telp 
        self.email = email 
        self.deskripsi = deskripsi 

class KontakApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Kontak")
        self.listkontak = []
        self.create_widgets()

    def create_widgets(self):
        labels = ["Nama:", "No. Telepon:", "Email:", "Deskripsi:"]
        for i, label_text in enumerate(labels):
            tk.Label(self.root, text=label_text).grid(row=i, column=0)        
        self.entry_fields = [tk.Entry(self.root) for _ in range(len(labels))]        
        for i, entry in enumerate(self.entry_fields): 
            entry.grid(row=i, column=1)        
        button_texts = ["Tambah Kontak", "Hapus Kontak", "Simpan ke File"] 
        perintah = [self.add_kontak, self.delete_kontak, self.Print] 
        for i, (text, command) in enumerate(zip(button_texts, perintah), start=len(labels)):
            tk.Button(self.root, text=text, command=command).grid(row=i, column=0, columnspan=2, pady=5)  
        self.kontak_listbox = tk.Listbox(self.root, width=50)
        self.kontak_listbox.grid(row=0, column=2, rowspan=len(labels)) 

    def add_kontak(self):
        values = [entry.get() for entry in self.entry_fields]
        if all(values): 
            kontak = Kontak(*values)  
            self.listkontak.append(kontak)  
            self.update_kontak_listbox()
            self.clear_entry_fields()  
            messagebox.showinfo("Pemberitahuan", "Data berhasil ditambahkan!") 
        else:
            messagebox.showwarning("Peringatan", "Semua kolom harus diisi!")  

    def delete_kontak(self):
        selected_index = self.kontak_listbox.curselection()
        if selected_index:
            del self.listkontak[selected_index[0]]  
            self.update_kontak_listbox()  
            messagebox.showinfo("Pemberitahuan", "Data berhasil dihapus!") 

    def update_kontak_listbox(self):
        self.kontak_listbox.delete(0, tk.END) 
        for kontak in self.listkontak:
            self.kontak_listbox.insert(tk.END, f"{kontak.nama} - {kontak.no_telp} - {kontak.email} - {kontak.deskripsi}")

    def clear_entry_fields(self):
        for entry in self.entry_fields:
            entry.delete(0, tk.END)  

    def Print(self):
        with open("kontak-saya.txt", "w") as file:
            for kontak in self.listkontak:
                file.write(f"{kontak.nama}, {kontak.no_telp}, {kontak.email}, {kontak.deskripsi}\n")
            messagebox.showinfo("Pemberitahuan", "Data berhasil disimpan ke kontak-saya.txt!") 

root = tk.Tk()  
app = KontakApp(root)  
root.mainloop()  