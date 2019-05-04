def cetak_gambar(panjang):
    if panjang%2==0 or panjang<2:
        raise Exception('Input hari berupa bilangan bulat positif ganjil')
    for i in range(panjang):
        if i+1==(panjang+1)//2:
            print((panjang-1)*'* '+'*')
        else:
            print('* '+(panjang-2)*'= '+'*')
