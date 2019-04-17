roman = input()
number = 0
romans = 'IVXLCDM'
nums = [1,5,10,50,100,500,1000]
r2n = {}
for r, n in zip(romans, nums):
    r2n[r] = n

for i, digi in enumerate(roman):
    number += r2n[digi]
    previous = roman[i-1:i+1]
    if previous  == 'IV':
        number -= 2
    if previous  == 'IX':
        number -= 2
    if previous  == 'IL':
        number -= 2
    if previous  == 'IC':
        number -= 2
    if previous  == 'ID':
        number -= 2
    if previous  == 'IM':
        number -= 2
    if previous  == 'XL':
        number -= 20
    if previous  == 'XC':
        number -= 20
    if previous  == 'XD':
        number -= 20
    if previous  == 'XM':
        number -= 20
    if previous  == 'CD':
        number -= 200
    if previous  == 'CM':
        number -= 200
print(number)