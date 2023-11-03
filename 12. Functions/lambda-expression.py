def get_full_name(first_name, last_name, formatter) :
    return formatter(first_name, last_name)

fullname = get_full_name('Rizki', 'Darmawan', lambda first_name, last_name : f'{first_name} {last_name}')

print(fullname)

def times (n):
    return lambda x : x * n

double = times(2)
result = double(2)

tripel = times(3)
result2 = tripel(3)
print(result)
print(result2)

print('####################################')

callables = []

for i in (1, 2, 3) :
    callables.append(lambda a=i : a)

for f in callables :  
    print(f())

