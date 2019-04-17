#9:17-
sx,sy,tx,ty=map(int,input().split())
tx-=sx
ty-=sy
ans=""
ans+="R"*tx+"U"*ty
ans+="L"*tx+"D"*ty
ans+="D"+"R"*(tx+1)+"U"*(ty+1)+"L"
ans+="U"+"L"*(tx+1)+"D"*(ty+1)+"R"
print(ans)

#方針：n往復するときに被らないで行くには+いくつ必要か考える
#実装方法：(tx,ty)-(sx,sy)の差分を考えてそれの掛け算

