x = int(input())
print(sum(list(map(int,list(str(x))))))


#参考
print(str(x))
print(list(str(x)))
print(map(int, list(str(x))))
print(list((map(int, list(str(x))))))


