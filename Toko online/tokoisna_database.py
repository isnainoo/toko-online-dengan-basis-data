from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root', database='dbtokoonline')
cursor = cnx.cursor()

# Membuat tabel-tabel
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pelanggan (
        id_pelanggan INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        nama VARCHAR(100) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        telepon VARCHAR(20) NOT NULL,
        alamat TEXT NOT NULL
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Barang (
        id_barang CHAR(4) NOT NULL PRIMARY KEY,
        nama_barang VARCHAR(40) NOT NULL,
        harga DECIMAL(10, 2) NOT NULL,
        stok INT NOT NULL
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Karyawan (
        id_karyawan CHAR(4) NOT NULL PRIMARY KEY,
        nama_karyawan VARCHAR(100) NOT NULL,
        jabatan VARCHAR(50) NOT NULL,
        gaji DECIMAL(10, 2) NOT NULL
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Transaksi (
        id_transaksi INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        id_pelanggan INT NOT NULL,
        id_barang CHAR(4) NOT NULL,
        id_karyawan CHAR(4) NOT NULL,
        jumlah INT NOT NULL,
        tanggal DATETIME NOT NULL,
        FOREIGN KEY (id_pelanggan) REFERENCES Pelanggan(id_pelanggan),
        FOREIGN KEY (id_barang) REFERENCES Barang(id_barang),
        FOREIGN KEY (id_karyawan) REFERENCES Karyawan(id_karyawan)
    )
''')

cnx.commit()
cnx.close()