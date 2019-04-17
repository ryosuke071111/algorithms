with open('data1.txt') as f:
  nums = f.readlines()       #行ごとに読み込んでリスト化
  nums="".join(nums).split("\n")
  nums.pop()
  nums=list(map(lambda x:x.strip("(",).strip(')'),nums))
  nums=[i.split(",") for i in nums]
  biggest=0
  for i,j in enumerate(nums):
    if int(nums[i][1])>int(nums[biggest][1]):
      biggest=i
  print(nums[biggest])




