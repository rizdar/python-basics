def greet() :
    '''Display a greeting to users'''
    print('hi')

greet()

def introduce(name, age) :
    person = f'hello, my name is {name}, and i\'m {age} years old'
    print(person)

introduce('Rizki', 27)

name = 'Rizki'
birth_year = 1996

def kenalan(name, birthyear) :
    current_year = 2023
    age =  current_year - birthyear
    message = f'Hello, my name is {name}, and im {age} years old'
    print(message)

kenalan(name, birth_year)
