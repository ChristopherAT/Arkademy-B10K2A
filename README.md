# Arkademy-B10K2A
Jawaban soal seleksi Bootcamp 10 Arkademy

Gunakan online IDE berikut untuk mencoba program soal_1 sampai soal_5
https://repl.it/languages/python3

Pembahasan soal nomor 1:
.........................
.........................
.........................
.........................
.........................
.........................

-----------------------------------------------------------------------------------
Soal nomor 2:
Pada sebuah form, terdapat 3 buah field yaitu: username, dan password.
Buatlah function untuk memvalidasi field-field tersebut, dengan requirement 
sebagai berikut:
- Username, merupakan kombinasi dari huruf kecil. Dengan panjang tepat 8
karakter.
- Password, merupakan kombinasi dari huruf kecil, huruf besar, angka, dan
karakter spesial. Dengan panjang minimal 8 karakter.
Clue:
Peserta hanya diminta membuat function validasi, tidak perlu membuat form HTML.
examples:
- is_username_valid(‘zeronull’)
Return true
- is_username_valid(‘useroke’)
Return false
- is_password_valid(‘qazW_123’)
Return true

Jawaban:
Pertama, asumsikan karakter spesial yang diboleh digunakan sebagai password 
adalah semua simbol yang dapat diprint (ada di keyboard) kecuali spasi.
Spasi tidak digunakan dalam password karena jika ada spasi berurutan, sulit 
untuk menghitung jumlah karakternya.

Untuk validasi username, digunakan fungsi validasiUser dengan satu input berupa string.
Output yang dihasilkan adalah True atau False.

-----------------------------------------------------------------------------------
Soal nomor 3:
Buatlah function untuk mencetak gambar seperti dibawah ini, yang mempunyai
sebuah parameter sebagai panjang lebar/tinggi gambar. Parameter harus merupakan
bilangan ganjil:
Misalnya jika dijalankan:
cetak_gambar(5);
Makan akan dihasilkan:
* = = = *
* = = = *
* * * * *
* = = = *
* = = = *

Jawaban:
Program dibuat dengan bahasa Python 3.
contoh output dengan input lain:

cetak_gambar(3)
* = *
* * *
* = *

cetak_gambar(7)
* = = = = = *
* = = = = = *
* = = = = = *
* * * * * * *
* = = = = = *
* = = = = = *
* = = = = = *

-----------------------------------------------------------------------------------
Soal nomor 4:


