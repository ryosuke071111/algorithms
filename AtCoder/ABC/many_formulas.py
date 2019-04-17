n = 0
nums = []

def dfs(i,num):
  if (i==n-1):
    nums.append(num)
    return False
  if (dfs(i+1,num+'+')):
    return True
  if (dfs(i+1, num + '_')):
    return True
  return False

def calc():
  ans = 0
  p = 0
  for num in nums:
    print(num)
    for i in range(n):
      if (i==n-1):
        ans += int(s[p:n])
      elif (num[i]=='+'):
        ans += int(s[p:i+1])
        p = i + 1
    p = 0

  return ans

s = input()
n = len(s)
dfs(0,"")
print(calc())
