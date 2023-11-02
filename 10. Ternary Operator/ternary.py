# age = input('Silahkan masukan umur anda :')

# # if int(age) >= 18:
# #     ticket_price = 20000
# # else :
# #     ticket_price = 5000

# ticket_price = 20000 if int(age) >= 18 else 5000

# print(f'the ticket price is {ticket_price}')


def harga_tickets(umur) :
    if umur >= 18 :
        harga = 20000
    else :
        harga = 5000
    print(f'Harga ticket untuk anda adalah : {harga}')

# umur = input('Silahkan masukkan umur anda :')
harga_tickets(8)

jarak = 60
status = 'Jauh' if jarak > 100 else 'Dekat'
print(status)








