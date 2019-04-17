def convert4(num):
  ans=0
  for i in range(len(num)):
    ans+=int(num[i])*(4**i)
  return ans
num=input()[::-1]
print(convert4(num))
