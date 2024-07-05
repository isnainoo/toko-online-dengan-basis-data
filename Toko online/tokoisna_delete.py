import mysql.connector

# Koneksi ke database
cnx = mysql.connector.connect(user='root', database='dbtokoonline')
cursor = cnx.cursor()

# Menghapus data terkait di tabel transaksi
cursor.execute('''
        DELETE FROM transaksi
        WHERE id_barang = 'BR10'
    ''')

# Delete data pada tabel Barang
cursor.execute('''
    DELETE FROM Barang
    WHERE id_barang = 'BR10'
''')

# Menghapus data terkait di tabel transaksi
cursor.execute('''
        DELETE FROM transaksi
        WHERE id_karyawan = 'KRA3'
    ''')

# Delete data pada tabel Karyawan
cursor.execute('''
    DELETE FROM Karyawan
    WHERE id_karyawan = 'KRA3'
''')

# Delete data pada tabel Pelanggan
cursor.execute('''
    DELETE FROM Pelanggan
    WHERE id_pelanggan = 10
''')

cnx.commit()
cnx.close()