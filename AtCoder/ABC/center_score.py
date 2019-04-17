n = int(input())
anss = list(input())
anss = ','.join(anss)

maxnum = max(anss.count("1"),anss.count("2"),anss.count("3"),anss.count("4"))
minnum = min(anss.count("1"),anss.count("2"),anss.count("3"),anss.count("4"))

print(maxnum, minnum)
