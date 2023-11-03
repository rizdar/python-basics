def greeting(name, message= 'hello') :
    pesan = f'{message} {name}'
    return pesan

greeting1 = greeting('Rizki')
print(greeting1)
greeting2 = greeting(message='hi', name='Rizki')
print(greeting2)

