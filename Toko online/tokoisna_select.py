import mysql.connector

def view_data():
    cnx = mysql.connector.connect(user='root', database='dbtokoonline')
    cursor = cnx.cursor()

    # Fungsi menampilkan data 
    def view_pelanggan():
        query = "SELECT * FROM Pelanggan"
        cursor.execute(query)
        result = cursor.fetchall()
        print("Data Pelanggan:")
        for row in result:
            print(row)
        print("\n")

    def view_barang():
        query = "SELECT * FROM Barang"
        cursor.execute(query)
        result = cursor.fetchall()
        print("Data Barang:")
        for row in result:
            print(row)
        print("\n")

    def view_karyawan():
        query = "SELECT * FROM Karyawan"
        cursor.execute(query)
        result = cursor.fetchall()
        print("Data Karyawan:")
        for row in result:
            print(row)
        print("\n")

    def view_transaksi():
        query = "SELECT * FROM Transaksi"
        cursor.execute(query)
        result = cursor.fetchall()
        print("Data Transaksi:")
        for row in result:
            print(row)
        print("\n")

    

    # Menampilkan data dari setiap tabel
    view_pelanggan()
    view_barang()
    view_karyawan()
    view_transaksi()
    
    cnx.close()

view_data()