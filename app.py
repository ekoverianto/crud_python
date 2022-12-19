import mysql.connector
import os

# MEMBUAT DRIVER MYSQL 
db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'db_akademik'
)

# CEK KONEKSI
# if db.is_connected():
#     print('Terkoneksi')
# else:
#     print('Gagal Terkoneksi')

# CREATE DATA
def create(db):
    npm = int(input('Masukan NPM: '))
    nama = str(input('Masukan Nama: '))
    jurusan = str(input('Masukan Jurusan: '))

    cursor = db.cursor()
    value = (npm, nama, jurusan)
    sql = 'INSERT INTO tb_mhs (npm, nama, jurusan) VALUES (%s,%s,%s)'

    cursor.execute(sql, value)
    db.commit()
    print('{} data berhasil disimpan'.format(cursor.rowcount))


# READ DATA
def read(db):
    cursor = db.cursor()
    sql = 'SELECT * FROM tb_mhs'
    cursor.execute(sql)
    r = cursor.fetchall()
    if cursor.rowcount == 0:
        print('Data Tidak Ada')
    else:
        for data in r:
            print(data)

# UPDATE DATA
def update(db):
    read(db) # panggil fungsi read untuk mengecek data mana yang akan diubah
    _npm = int(input('Masukan NPM data yang akan di ubah: '))
    nama = str(input('Masukan Nama: '))
    jurusan = str(input('Masukan Jurusan: '))

    cursor = db.cursor()
    sql = 'UPDATE tb_mhs SET nama=%s, jurusan = %s WHERE npm=%s'
    value = (nama, jurusan, _npm)
    cursor.execute(sql, value)
    db.commit()
    print('{} data berhasil diubah'.format(cursor.rowcount))
    read(db) # panggil fungsi read untuk melihat hasil perubahan

# DELETE DATA 
def delete(db):
    read(db)
    _npm = int(input('Pilih NPM data yang akan di hapus: '))
    cursor = db.cursor()
    sql = 'DELETE FROM tb_mhs WHERE npm=%s'
    value = (_npm,)
    cursor.execute(sql, value)
    db.commit()
    print('{} data berhasil dihapus'.format(cursor.rowcount))
    read(db)

def menu(db):
    print('____PILIH MENU____')
    print('1. Tambah Data')
    print('2. Tampil Data')
    print('3. Ubah Data')
    print('4. Hapus Data')
    print('0. Keluar')
    print('------------------')

    menu = int(input('Masukan Menu: '))

    # os.system('cls') # untuk windows
    os.system('clear')

    if menu == 1:
        create(db)
    elif menu == 2:
        read(db)
    elif menu == 3:
        update(db)
    elif menu == 4:
        delete(db)
    elif menu == 0:
        exit()
    else:
        print('Menu Tidak Ada')

if __name__ == '__main__':
    while(True):
        menu(db)
