import mysql.connector

def view_data():
    cnx = mysql.connector.connect(user='root', database='dbtokoonline')
    cursor = cnx.cursor()

    def view_pelanggan():
        query = "SELECT * FROM Pelanggan"
        cursor.execute(query)
        result = cursor.fetchall()
        print("Data Pelanggan:")
        for row in result:
            print(row)
        print("\n")
        
    def view_pelanggan():
        query = "SELECT nama, id_barang from pelanggan join transaksi on pelanggan.id_pelanggan = transaksi.id_pelanggan"
        cursor.execute(query)
        result = cursor.fetchall()
        print("Data Pelanggan:")
        for row in result:
            print(row)
        print("\n")

    view_pelanggan()
    cnx.close()

view_data()