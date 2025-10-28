import getpass
from pembeli import pembeli
from penjual import penjual
from data import database

panjangInisialDatabase = int(len(database))

def register():

    print("\n--- Halaman Registrasi ---")
    username = input("Username (tanpa spasi)   : ")
    
    # Buat dan Cek Username
    for cekUser in database:
        if cekUser["username"] == username:
            print("Username udah ada.")
            return
    # Buat Pasword
    password = getpass.getpass("Buat Password            : ")
    cekPassword = getpass.getpass("Masukkan kembali password: ")
    if password != cekPassword:
        return
    # Pilih Role
    print("Role:\n1. Pembeli\n2. Penjual")
    RolePilihan = input("Pilih Role: ")
    role = ""
    if RolePilihan == '1':
        role = "Pembeli"
    elif RolePilihan == '2':
        role = "Penjual"
    else:
        print("Pilih role yang benar")
        return
        
    # konstruksi data akun baru
    idUserBaru = len(database)
    userBaru = {
        "user_id": idUserBaru,
        "username": username,
        "password": password,
        "role": role,
        "saldo": 0
    }
    
    # masukkan data akun baru ke database
    database.append(userBaru)
    print(f"Registrasi berhasil! Silakan login, {username}")


def login():
    print("\n--- Halaman Login ---")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    
    # Cari input username di database
    for cekUser in database:
        if cekUser["username"] == username and cekUser["password"] == password:
            print(f"Login berhasil! {username}")
            idnya = cekUser["user_id"]
            
            while True:
                # Ke menu sesuai role
                if cekUser["role"] == "Pembeli":
                    # Cek jika dari sana minta keluar
                    if pembeli(database[idnya]) == "keluar":
                        return

                elif cekUser["role"] == "Penjual":
                    # Cek jika dari sana minta keluar
                    if penjual(database[idnya]) == "keluar":
                        return
            
    # Kalau user dan password tidak ditemukan
    print("Username atau password salah.")
    
################################################################################################
# Bagian utama kode

def main():
    while True:
        print('''
========================
|    Ini E-Commerce    |
========================
1. Login
2. Register
3. Keluar''')
        # Input user ke menu mana
        pilihan = input("Pilih 1/2/3: ")
        if pilihan == '1':
            login()
        elif pilihan == '2':
            register()
        elif pilihan == '3':
            print("Terima kasih!")
            break 
        # Jika input tidak sesuai
        else:
            print("Pilihan tidak valid.")

# Run main()
if __name__ == "__main__":
    main()