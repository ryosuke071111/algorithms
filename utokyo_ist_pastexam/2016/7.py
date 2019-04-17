spellings_1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
spellings_101 = ['eleven', 'twelve', 'thirdteen', 'forteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'ninteen']
spellings_10 = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninty']
s2n = {}
for i,s in enumerate(spellings_1):
    s2n[s] = i+1
for i,s in enumerate(spellings_101):
    s2n[s] = i+1+10
for i,s in enumerate(spellings_10):
    s2n[s] = (i+1)*10
# for key, val in s2n.items():
#     print(f'{key} : {val}')
multiplier = ['hundred', 'thousand']


a= 'fifty four thousand three hundred twenty five'
words = a.split(' ')
number = 0
temp = 0
for i, word in enumerate(words):
    if word in s2n.keys():
        temp += s2n[word]

    if word in multiplier:
        # multiplier_encountered = True
        if word == 'hundred':
            number += temp * 100
        else:
            number += temp * 1000
        temp = 0
        continue

    if i == len(words) - 1:#last word
        number += temp
print(f'Result : {number}')
