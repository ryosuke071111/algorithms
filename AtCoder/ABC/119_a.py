# s=input().split('/')
# if int(s[0])<=2019 and int(s[1])<=4 and int(s[2])<=30:
#   print('Heisei')
# else:
#   print('TBD')

s=input()
print('Heisei' if s<="2019/04/30" else "TBD")
