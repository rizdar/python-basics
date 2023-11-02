for index in  range(10) :
    print(index) 
    if index == 3 :
        break

print('########@@@@@@@')

for x in range(5) :
    for y in range(5) :
        if y > 1 :
            break
        print(f'({x}, {y})')

print('########@@@@@@@')

while True :
    color = input('Enter your favorite color :')
    if color.lower() == 'quit' :
        break