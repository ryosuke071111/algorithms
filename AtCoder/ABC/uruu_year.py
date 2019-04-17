y =int(input())

judge = 'NO'

if y % 4 == 0:
  judge = 'YES'

if y % 100 == 0:
  judge = 'NO'

if y % 400 == 0:
  judge = 'YES'

#in pipleline action, change flag in binary value.
print(judge)
