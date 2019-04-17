#9:09-
# s=input().split("+")
# count=0
# for i in s:
#   if "0" not in i:
#     count+=1
# print(count)

print(len([i for i in input().split("+") if not "0" in i]))
