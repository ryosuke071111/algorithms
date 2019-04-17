a,b,c = map(int,input().split())
candies =[a,b,c]
print('Yes' if max(candies) == sum(candies)-max(candies) else 'No')
