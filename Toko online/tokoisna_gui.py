import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Fungsi untuk menambahkan pelanggan ke database
def tambah_pelanggan():
    nama, email, telepon, alamat = entry_nama.get(), entry_email.get(), entry_telepon.get(), entry_alamat.get("1.0", tk.END)
    try:
        cursor.execute("INSERT INTO Pelanggan (nama, email, telepon, alamat) VALUES (%s, %s, %s, %s)", (nama, email, telepon, alamat))
        cnx.commit()
        messagebox.showinfo("Sukses", "Pelanggan berhasil ditambahkan ke database!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Fungsi untuk menambahkan transaksi ke database
def tambah_transaksi():
    nama_pelanggan, jumlah, barang, id_karyawan = entry_nama_pelanggan.get(), entry_jumlah.get(), selected_barang.get(), selected_karyawan.get()
    try:
        cursor.execute(
            "INSERT INTO Transaksi (id_pelanggan, id_barang, id_karyawan, jumlah, tanggal) VALUES ((SELECT id_pelanggan FROM Pelanggan WHERE nama = %s), (SELECT id_barang FROM Barang WHERE nama_barang = %s), %s, %s, NOW())",
            (nama_pelanggan, barang, id_karyawan, jumlah)
        )
        cnx.commit()
        messagebox.showinfo("Sukses", "Transaksi berhasil ditambahkan ke database!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Fungsi untuk memperbarui daftar barang
def update_barang_options():
    cursor.execute("SELECT nama_barang FROM Barang")
    options = cursor.fetchall()
    selected_barang.set('')
    menu = barang_menu['menu']
    menu.delete(0, 'end')
    for option in options:
        menu.add_command(label=option[0], command=lambda value=option[0]: selected_barang.set(value))

# Koneksi ke database
try:
    cnx = mysql.connector.connect(user='root', database='dbtokoonline')
    cursor = cnx.cursor()
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit(1)

root = tk.Tk()
root.title("Selamat Berbelanja di TOKOISNA")

# Frame untuk input pelanggan
frame_pelanggan = tk.LabelFrame(root, text="Masukkan Identitas Anda")
frame_pelanggan.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

fields = [("Nama:", tk.Entry(frame_pelanggan, width=30)),
          ("Email:", tk.Entry(frame_pelanggan, width=30)),
          ("Telepon:", tk.Entry(frame_pelanggan, width=30)),
          ("Alamat:", tk.Text(frame_pelanggan, width=30, height=5))]

for i, (label, entry) in enumerate(fields):
    tk.Label(frame_pelanggan, text=label).grid(row=i, column=0, padx=10, pady=5)
    entry.grid(row=i, column=1, padx=10, pady=5)

entry_nama, entry_email, entry_telepon, entry_alamat = [entry for _, entry in fields]

tk.Button(frame_pelanggan, text="Kirim Identitas", command=tambah_pelanggan).grid(row=len(fields), columnspan=2, padx=10, pady=10, sticky="ew")

# Frame untuk input transaksi
frame_transaksi = tk.LabelFrame(root, text="Pilih Transaksi")
frame_transaksi.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

tk.Label(frame_transaksi, text="Ketik Nama Anda:").grid(row=0, column=0, padx=10, pady=5)
entry_nama_pelanggan = tk.Entry(frame_transaksi, width=30)
entry_nama_pelanggan.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_transaksi, text="Pilih Barang:").grid(row=1, column=0, padx=10, pady=5)
selected_barang = tk.StringVar()
barang_menu = tk.OptionMenu(frame_transaksi, selected_barang, ())
barang_menu.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_transaksi, text="Jumlah:").grid(row=2, column=0, padx=10, pady=5)
entry_jumlah = tk.Entry(frame_transaksi, width=30)
entry_jumlah.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame_transaksi, text="ID Karyawan:").grid(row=3, column=0, padx=10, pady=5)
selected_karyawan = tk.StringVar()
karyawan_menu = tk.OptionMenu(frame_transaksi, selected_karyawan, "KRA1", "KRA2","KRA3")
karyawan_menu.grid(row=3, column=1, padx=10, pady=5)

tk.Button(frame_transaksi, text="Tambah Transaksi", command=tambah_transaksi).grid(row=4, columnspan=2, padx=10, pady=10, sticky="ew")

update_barang_options()
root.mainloop()

cursor.close()
cnx.close()