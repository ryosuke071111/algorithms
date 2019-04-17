a = input()
number = int(a)


romans = 'IVXLCDM'
nums = [1,5,10,50,100,500,1000]
r2n = {}
n2r = {}
for r, n in zip(romans, nums):
    r2n[r] = n
    n2r[n] = r

num_str = str(number)
str_digi = len(str(number))
output = ''
for i, s in enumerate(num_str):
    digis = []
    s = int(s)
    if s <= 3:
        [digis.append(1) for _ in range(s)]
    elif s == 4:
        digis.append(1)
        digis.append(5)
    elif s <= 8:
        digis.append(5)
        [digis.append(1) for _ in range(s - 5)]
    else:
        digis.append(1)
        digis.append(10)
    current_digi = (str_digi - i)
    if current_digi == 4:
        oner, fiver, tener = 'M', '', ''
    if current_digi == 3:
        oner, fiver, tener = 'C', 'D', 'M'
    if current_digi == 2:
        oner, fiver, tener = 'X', 'L', 'C'
    if current_digi == 1:
        oner, fiver, tener = 'I', 'V', 'X'
    for d in digis:
        if d == 1:
            output += oner
        elif d == 5:
            output += fiver
        elif d == 10:
            output += tener
print(f'Output {output}')
    
    
