n = int(input())


# sump =[]

# for i in range(1,n+1):
#   sump.append(i*10000*(1/n))

print(int(sum([i*10000/n for i in range(1,n+1)])))

#forの中に入れる処理を頭に入れることでリスト内表記とできる
