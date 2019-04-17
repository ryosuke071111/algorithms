import matplotlib.pyplot as plt

with open('data1.txt') as f:
  nums = f.readlines()       #行ごとに読み込んでリスト化
  nums="".join(nums).split("\n")
  nums.pop()
  nums=list(map(lambda x:x.strip("(",).strip(')'),nums))
  nums=[i.split(",") for i in nums]
  x=[int(i[0]) for i in nums]
  y=[int(i[1]) for i in nums]
  plt.scatter(x,y)
  # plt.xlabel("Leprechauns")
  # plt.ylabel("Gold")
  plt.show()
