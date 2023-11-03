def add_number(a, b) :
    num = a + b
    return num

print(add_number(9, 3))

def cek_barang(nama) :
    if nama == 'Kopi':
        return f'barang habis'
    elif nama == 'Susu' :
        return f'barang sisa sedikit'
    else :
        return 'Bagusssohuhoh'

print(cek_barang(input('isi')))