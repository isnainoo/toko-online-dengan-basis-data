import mysql.connector
from datetime import datetime

cnx = mysql.connector.connect(user='root', database='dbtokoonline')
cursor = cnx.cursor()

# Data untuk tabel 
pelanggan = [
    (1,"Nadiya Poetri", "Nadiya@gmail.com", "085734567890", "Jl. Kebon Jeruk No. 1"),
    (2,"Laila Nabila", "laila@gmail.com", "085734567891", "Jl. Mangga No. 2"),
    (3,"Alice Nafilah", "alice@gmail.com", "085734567892", "Jl. Sudirman No. 3"),
    (4,"Melinda Santi", "Melin@gmail.com", "085743482338", "Jl. Thamrin No. 9"),
    (5,"Mahendra Rafli", "rafli@gmail.com", "085734567594", "Jl. Sudirman No. 4"),
    (6,"Nino Biyan", "nino@gmail.com", "085734567863", "Jl. Kebon jeruk No. 4"),
    (7,"Adisty Aisya", "adisya@gmail.com", "085734562223", "Jl. Kuningan No. 4"),
    (8,"Melisa Nasyifa", "melisa@gmail.com", "085734534890", "Jl. Thamrin No. 4"),
    (9,"Rehan lambun", "rehan@gmail.com", "085734567891", "Jl. Sudirman No. 2"),
    (10,"Reha Sasya", "rehassy@gmail.com", "085734567894", "Jl. Kuningan No. 5")
]

barang = [
    ('BR01', "Buku", 8000.00, 800),
    ('BR02', "Pulpen", 4000.00, 200),
    ('BR03', "Pensil", 3000.00, 150),
    ('BR04', "Penggaris", 6000.00, 100),
    ('BR05', "Kertas Asturo", 6500.00, 100),
    ('BR06', "Pensil 2B", 5000.00, 400),
    ('BR07', "Stabilo", 10000.00, 600),
    ('BR08', "Buku Gambar", 12000.00, 400),
    ('BR09', "Krayon", 20000.00, 450),
    ('BR10', "Penghapus", 2000.00, 300)
]

karyawan = [
    ('KRM1', "Isna Choiron Nasikhin", "Manager", 10000000.00),
    ('KRM2', "Bara Prakoco", "Manager Produk", 6000000.00),
    ('KRU1', "Anselma Nur Hibinaya", "Supervisor", 7000000.00),
    ('KRD1', "Maya Marselina", "Analis Data", 6000000.00),
    ('KRD2', "Adinda Nurasyafira", "Analis Dara", 6000000.00),
    ('KRA1', "Salwa Salsabila", "Staff", 4500000.00),
    ('KRA2', "Odet Badra Sentosa", "Staff", 4000000.00),
    ('KRA3', "Juna Pamungkas", "Staff", 4000000.00),
    ('KRC1', "Rifat Abdul karim", "Courier", 4000000.00),
    ('KRC2', "Pambayun Saputro", "Courier", 4000000.00)
]

transaksi = [
    (1, 'BR01', 'KRA2', 10, datetime(2024, 6, 23, 10, 0)),
    (2, 'BR02', 'KRA1', 20, datetime(2024, 6, 24, 11, 0)),
    (3, 'BR03', 'KRA2', 15, datetime(2024, 6, 25, 12, 0)),
    (4, 'BR04', 'KRA3', 10, datetime(2024, 6, 26, 13, 0)),
    (5, 'BR05', 'KRA2', 25, datetime(2024, 6, 27, 12, 0)),
    (6, 'BR06', 'KRA1', 5, datetime(2024, 6, 27, 14, 0)),
    (7, 'BR07', 'KRA2', 30, datetime(2024, 6, 27, 16, 0)),
    (8, 'BR08', 'KRA3', 35, datetime(2024, 6, 27, 16, 0)),
    (9, 'BR09', 'KRA2', 50, datetime(2024, 6, 27, 18, 0)),
    (10, 'BR10', 'KRA1', 70, datetime(2024, 6, 27, 19, 0))
]

# Memasukkan data ke tabel 
for data in pelanggan:
    cursor.execute('''
        INSERT INTO Pelanggan (id_pelanggan, nama, email, telepon, alamat)
        VALUES ( %s, %s, %s, %s, %s)
    ''', data)

for data in barang:
    cursor.execute('''
        INSERT INTO Barang (id_barang, nama_barang, harga, stok)
        VALUES (%s, %s, %s, %s)
    ''', data)

for data in karyawan:
    cursor.execute('''
        INSERT INTO Karyawan (id_karyawan, nama_karyawan, jabatan, gaji)
        VALUES (%s, %s, %s, %s)
    ''', data)

for data in transaksi:
    cursor.execute('''
        INSERT INTO Transaksi (id_pelanggan, id_barang, id_karyawan, jumlah, tanggal)
        VALUES (%s, %s, %s, %s, %s)
    ''', data)

cnx.commit()
cnx.close()