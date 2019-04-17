deg,dis = map(int,input().split())

def custom_round(number, ndigits=0):
    if type(number) == int:#整数ならそのまま返す
        return number
    d_point = len(str(number).split('.')[1])#小数点以下が何桁あるか定義
    if ndigits >= d_point:#求める小数点以下の値が引数より大きい場合はそのまま返す
        return number
    c = (10 ** d_point) * 2
    #小数点以下の桁数分元の数に0を足して整数にして2倍するための値(0.01ならcは200)
    return round((number * c + 1) / c, ndigits)
    #元の数に0を足して整数にして2倍して1を足して2で割る。元の数が0.01なら0.015にしてroundを行う


dirr = custom_round((deg / 10),2)

if 11.25<= dirr < 33.75:
  dirr = 'NNE'
elif 33.75<= dirr < 56.25:
  dirr = 'NE'
elif 56.25<= dirr < 78.75:
  dirr = 'ENE'
elif 78.75<= dirr < 101.25:
  dirr = 'E'
elif 101.25<= dirr < 123.75:
  dirr = 'ESE'
elif 123.75<= dirr < 146.25:
  dirr = 'SE'
elif 146.25<= dirr < 168.75:
  dirr = 'SSE'
elif 168.75<= dirr < 191.25:
  dirr = 'S'
elif 191.25<= dirr < 213.75:
  dirr = 'SSW'
elif 213.75<= dirr < 236.25:
  dirr = 'SW'
elif 236.25<= dirr < 258.75:
  dirr = 'WSW'
elif 258.75<= dirr < 281.25:
  dirr = 'W'
elif 281.25<= dirr < 303.75:
  dirr = 'WNW'
elif 303.75<= dirr < 326.25:
  dirr = 'NW'
elif 326.25<= dirr < 348.75:
  dirr = 'NNW'
else:
  dirr = 'N'

w = custom_round((dis/60),1)

if 0.0<= w<= 0.2:
  w = 0
elif 0.3<= w<= 1.5:
  w = 1
elif 1.6<= w<= 3.3:
  w = 2
elif  3.4<= w <= 5.4:
  w = 3
elif  5.5<= w <= 7.9:
  w = 4
elif  8.0<= w <= 10.7:
  w = 5
elif  10.8<= w <= 13.8:
  w = 6
elif  13.9<= w <= 17.1:
  w = 7
elif  17.2<= w <= 20.7:
  w = 8
elif  20.8<= w <= 24.4:
  w = 9
elif  24.5<= w <= 28.4:
  w = 10
elif  28.5<= w <= 32.6:
  w = 11
elif  32.7<= w:
  w = 12

if w ==0:
  dirr = 'C'


print(dirr,w)



#別解
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
deg, dis = map(int, input().split())
degrees = ['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW']
Tdeg = 'N'
if 112.5 <= deg < 3487.5:
    degIndex = int(round(deg / 225, 0))
    Tdeg = degrees[degIndex]

#ms = float(Decimal(str(dis/60)).quantize(Decimal('0.1'), rounding = ROUND_HALF_UP))
ms = int((dis/60+0.05)*10+0.0001)/10
winds = [0.2,1.5,3.3,5.4,7.9,10.7,13.8,17.1,20.7,24.4,28.4,32.6]
winds.append(ms)リスト
winds.sort()
Twind = winds.index(ms)

Tdeg = 'C' if Twind == 0 else Tdeg
print(Tdeg, Twind)


deg, dis~

tag ~
if 225 <= deg < de:
  defindex = int(roucn(deg/225,0))
  tdeg = degrsee[defindex]

ms = int(dis/60+0.05)*10+0.0001/10
winds = [34.3;ektlam,a]
winds.append()
winds,sor()
Twind = wind.index(ms)
#  既存の以下の数値を入れた
