# Arkademy-B10K2A
Jawaban soal seleksi Bootcamp 10 Arkademy

Gunakan online IDE berikut untuk mencoba program soal_1.py sampai soal_5.py

[Repl.it](https://repl.it/languages/python3).

## Soal nomor 1

## Soal nomor 2:
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

`- is_username_valid(‘zeronull’)`
Return true
`- is_username_valid(‘useroke’)`
Return false
`- is_password_valid(‘qazW_123’)`
Return true

# Jawaban nomor 2:
Pertama, asumsikan karakter spesial yang diboleh digunakan sebagai password 
adalah semua simbol yang dapat diprint (ada di keyboard) kecuali spasi.
Spasi tidak digunakan dalam password karena jika ada spasi berurutan, sulit 
untuk menghitung jumlah karakternya.

Untuk validasi username, digunakan fungsi `validasiUser` dengan satu input berupa string.
Output yang dihasilkan adalah True atau False.

## Soal nomor 3:
Buatlah function untuk mencetak gambar seperti dibawah ini, yang mempunyai
sebuah parameter sebagai panjang lebar/tinggi gambar. Parameter harus merupakan
bilangan ganjil:
Misalnya jika dijalankan:
`cetak_gambar(5);`
Makan akan dihasilkan:
```
* = = = *
* = = = *
* * * * *
* = = = *
* = = = *
```
# Jawaban nomor 3:
Program dibuat dengan bahasa Python 3.
contoh output dengan input lain:

```
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
```


## Soal nomor 4:
Buatlah sebuah function memiliki sebuah parameter berupa array yang berisi array yang
berisi abjad, yang mempunyai tugas untuk mengurutkan array terpendek ke terpanjang,
dan juga mengurutkan abjad di dalamnya dari a ke z. Dilarang menggunakan built in
function `array_multisort`

# Jawaban nomor 4:
Digunakan algoritma insertion sort yang dimodifikasi. Pertama, dilakukan sorting 
berdasarkan panjang array di dalam array. Bersamaan dengan proses sorting tersebut, 
jika ditemukan dua array dengan panjang yang sama, bandingkan tiap elemen array tersebut.
Membandingkan dua karakter mudah dilakukan dengan membandingkan nilai ASCII nya. Digunakan
fungsi `ord()` pada Python, misalnya huruf 'a' bernilai 97, 'b' bernilai 98, dst.
Diperoleh array dalam array yang terurut dari kecil ke besar.
Contoh:
Input 
`x=[['a'],['c'],['a','c'],['a'],['a','b'],['c','c','g'],['c','c','z']]`
Output
`[['a'], ['a'], ['c'], ['a', 'b'], ['a', 'c'], ['c', 'c', 'g'], ['c', 'c', 'z']]`

## Soal nomor 5:
Buatlah function yang mempunyai sebuah parameter, fungsi tersebut mempunyai tugas
untuk mencetak string acak sepanjang 32 karakter sebanyak jumlah parameter.
Pada function tersebut buatlah pengecekan untuk memastikan tidak ada
string(data) yang sama.
Clue:
Function dijalankan:
`cetak(3);`
Akan dicetak di layar
```
da2c312dfe804ef5bd318133a342251a
79n89a9mdfe804ef5b18133a342251o
6e576057da174c4189f7ea8341946aed
```

# Jawaban nomor 5
Untuk menghasilkan karakter random dengan panjang tertentu, digunakan fungsi hash.
Informasi lebih lanjut dapat dipelajari di (https://en.wikipedia.org/wiki/Hash_function).
Fungsi hash yang digunakan adalah SHA-256, implementasinya di Python diambil dari modul
hashlib. Untuk menghasilkan karakter random dengan SHA-256, diperlukan input. Input tersebut 
diambil secara acak dari fungsi time dalam modul time.

Dengan menggunakan fungsi hash SHA-256, dijamin tidak ada 2 karakter random yang sama persis. 
Lebih lanjutnya dapat dipelajari di (https://en.wikipedia.org/wiki/Birthday_attack).
Output dari fungsi hash SHA-256 adalah bilangan biner dengan panjang 256, sesuai dengan namanya.
Jika dituliskan dalam heksadesimal, panjangnya menjadi 64 karakter. Karena yang diminta hanya 32 
karakter, cukup diambil 32 karakter pertama.

Contoh hasil dari program:
Input: `cetak(10)`
Output:
```
c526c69431cf1db72d42fe89ed1936ea
201855209d5cab2cc23d028265080508
96fb42a9f7d25abcced003be415b650a
68c450b2a8fa258d73635e79a1608673
aab5afdb4097c28f03a8940185b91a40
457353821f32296bee519de78aba024a
19c28863be16683eb5171c92e5124e17
bf0817d71e631731e91194c278987f22
9960a1999f80cdeaec50ffdd7bfbcd88
7b6ea9a8c99624ad4e1d16bc05d1c81e
```



