def count_down(start)  :
    print(start)
    next = start - 1

    if next > 0 :
        count_down(next)

count_down(3)

def sum(n) :
    total = 0
    for index in range(n + 1) :
        print('index : ',  index)
        total += index
        print('total : ',  total)
    return total

result = sum(5)
print(result)

