def validasiUser(username):
    #Cek tipe variabel
    if not type(username) is str:
        print('Error: Input harus berupa string dalam tanda petik (\' \')')
        return False

    #Cek username
    if not len(username)==8:
        print('Error: Panjang username harus tepat 8 karakter')
        return False
    if not (username.isalpha() and username.islower()):
        print('Error: Username hanya boleh terdiri dari kombinasi huruf kecil')
        return False

    #Jika sampai tahap ini, username valid
    return True

def validasiPass(password):
    #Cek tipe variabel
    if not type(password) is str:
        print('Error: Input harus berupa string dalam tanda pertik (\' \')')
        return False

    #cek password
    if len(password)<7:
        print('Error: Panjang password minimal 8 karakter')
        return False
    if not password.isprintable() or ' ' in password:
        print('Error: Password hanya boleh terdiri dari huruf kecil, huruf besar, angka, dan karakter spesial tanpa spasi')
        return False

    #Jika sampai tahap ini, password valid
    return True
