import mysql.connector

cnx = mysql.connector.connect(user='root', database='dbtokoonline')
cursor = cnx.cursor()

# Update data pada tabel Pelanggan
cursor.execute('''
    UPDATE Pelanggan
    SET nama = 'Nadiya Putri'
    WHERE id_pelanggan = 1
''')
cursor.execute('''
    UPDATE Pelanggan
    SET alamat = 'Jl. Kebon Jeruk No.4'
    WHERE id_pelanggan = 2
''')

# Update data pada tabel Barang
cursor.execute('''
    UPDATE Barang
    SET stok = 400
    WHERE id_barang = 'BR10'
''')
cursor.execute('''
    UPDATE Barang
    SET stok = 700
    WHERE id_barang = 'BR06'
''')


# Update data pada tabel Transaksi
cursor.execute('''
    UPDATE Transaksi
    SET jumlah = 20, tanggal = '2024-06-26 14:00:00'
    WHERE id_transaksi = 4
''')
cursor.execute('''
    UPDATE Transaksi
    SET jumlah = 12, tanggal = '2024-06-24 18:20:00'
    WHERE id_transaksi = 9
''')
cursor.execute('''
    UPDATE Transaksi
    SET jumlah = 300, tanggal = '2024-06-27 20:20:00'
    WHERE id_transaksi = 10
''')



# Update data pada tabel Karyawan
cursor.execute('''
    UPDATE Karyawan
    SET jabatan = 'Senior Manager', gaji = '12000000.00'
    WHERE id_karyawan = 'KRM1'
''')
cursor.execute('''
    UPDATE Karyawan
    SET jabatan = 'Senior Staff', gaji = '5000000.00'
    WHERE id_karyawan = 'KRA1'
''')
cursor.execute('''
    UPDATE Karyawan
    SET jabatan = 'Senior Courier', gaji = '5000000.00'
    WHERE id_karyawan = 'KRC1'
''')
cursor.execute('''
    UPDATE Karyawan
    SET jabatan = 'Analis Data', gaji = '7000000.00'
    WHERE id_karyawan = 'KRD1'
''')
cursor.execute('''
    UPDATE Karyawan
    SET gaji = '7000000.00'
    WHERE id_karyawan = 'KRM2'
''')


cnx.commit()
cnx.close()