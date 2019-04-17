#通常のdfs（これだとTLE & WA）
# w,h = map(int,input().split())
# visited = [[False for i in range(w)] for i in range(h)]
# count = 0

# def dfs(i,j,visited):
#   global count
#   local_visit = visited[:]
#   if j + 1 < w:
#     dfs(i,j+1,local_visit)
#   if i + 1 < h:
#     dfs(i+1,j,local_visit)
#   if i == h-1 and j == w-1:
#     count += 1
#     return False


# dfs(0,0,visited)
# print(count)

#別解
def mod_pow(a,p,mod):
  if p == 0:
    return 1
  elif p%2 == 1:
    return a * mod_pow(a,p-1,mod)%mod
  else:
    d = mod_pow(a,p//2,mod)
  return d * d % mod

def mod_calc_comb(a,b,mod):
  if b>a-b:
    return mod_calc_comb(a,a-b,mod)
  ans_denom = 1
  ans_numer = 1

  for i in range(b):
    ans_denom *= (a-i)
    ans_numer *= (b-i)
    ans_denom %= mod
    ans_numer %= mod
  ans = ans_denom * mod_pow(ans_numer, mod-2,mod)%mod

  return ans
w,h = map(int,input().split())
mod = 10**9+7
ans = mod_calc_comb(h+w-2,h-1,mod)
print(ans)

#別解②
W, H = map(int, input().split())

mod = 10 ** 9 + 7

def fact(n):
    mod = 10 ** 9 + 7
    ans = 1
    for i in range(1, n+1):
        ans = ans * i % mod
    return ans

print(fact(W + H -2) * pow(fact(W-1), mod-2, mod) * pow(fact(H-1), mod-2, mod) % mod)

