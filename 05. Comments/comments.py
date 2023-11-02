price = 8000

#increase price by 5%
price *= 1.05

print(price)


salary = 8000000
salary *= 1.02 #increase salary by 2%

print(salary)

def saldo(salary, price) :
    sisa_uang = salary - price
    print(sisa_uang)

saldo(salary, price)