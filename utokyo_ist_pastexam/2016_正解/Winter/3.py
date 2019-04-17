def f(n, count=0):
    assert n >= 1
    assert isinstance(n, int)
    if n == 1:
        return 1, count
    else:   
        previous_value, count = f(n-1, count)
        value = (previous_value * 161 +  2457) % 2**24
        print(f'N : {n}, val : {value}, count : {count}')
        if value % 2 == 0 and n%2 == 1:
            count += 1
        return value, count

value, count = f(100)
print(value, count)


