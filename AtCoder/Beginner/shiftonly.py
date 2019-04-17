def fibonatch(a):
  list2=[1]
  n = 0
  x = 1
  y = 0
  z = 0
  while n < a:
    z = y
    y = x
    x = z + y
    n += 1
    list2.append(x)
  return list2

# n = input('個数入力')
# a = list(map(int, input().split()))
# cnt = 0
# while all(i%2==0 for i in a):
#   a = [i/2 for i in a]
#   cnt += 1
# print(cnt)
# list1=[i for i in range(30) if i == (i-1)*(i-2)]
# print(list1
list1 = [i**100 for i in (fibonatch(10000))]
print(list1)
