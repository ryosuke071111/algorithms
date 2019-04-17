import itertools
n=int(input())
count=0
nums=["3","5","7"]

k=3
while k <= len(str(n)):
  for i in itertools.product(nums,repeat=k):
    count_3=0
    count_5=0
    count_7=0
    if (int("".join(i))) <=n:
      for j in i:
        if j == "7":
          count_7+=1
        if j == "3":
          count_3+=1
        if j == "5":
          count_5+=1
      if count_5>=1 and count_3>=1 and count_7>=1:
        count+=1
  k+=1
print(count)

# for i in range(357,n+1,2):

#   if str(i)[0] != 3 or str(i)[0] != 5 or str(i)[0] != 7:
#     continue
#   if str(i)[-1] != 3 or str(i)[-1] != 5 or str(i)[-1] != 7:
#     continue
#   for j in str(i):
#     if j ==  "7":
#       count_7+=1
#     if j == "3":
#       count_3+=1
#     if j == "5":
#       count_5+=1
#   if count_5+count_3+count_7==len(str(i)):
#     if count_5>=1 and count_3>=1 and count_7>=1:
#       count+=1
# print(count)
