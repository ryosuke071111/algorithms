#許容誤差
EPS = 1e-10
#スカラー等号
def EQ(a,b):
    return (abs(a-b) < EPS)
#ベクトル等号
def EQV(x,y):
    return (EQ(x.real,y.real) and EQ(x.imag,y.imag) )

#単位ベクトル
def unit(a):
    return (a / abs(a))

#法線ベクトル
def normal(a):
    return ( a * (1j) , a*(-1j) )

#内積
def dot(a,b):
    return ( a.real * b.real + a.imag * b.imag )

#外積
def cross(a,b):
    return ( a.real * b.imag - a.imag * b.real )

#2直線の直交判定
def is_orthogonal(a,b):
    return EQ( dot(a,b) , 0.0)

#2直線の平行判定
def is_parallel(a,b):
    return EQ( cross(a,b) , 0.0)

#点cが直線ab上にあるか
def is_on_line(a,b,c):
    return EQ(cross(b-a,c-a), 0.0)

#点cが線分ab上にあるか
def is_on_line_seg(a,b,c):
    return (abs(a-c) + abs(c-b) < abs(a-b) + EPS)

#点cと直線abの距離
def distance_p_l(a,b,c):
    return (abs(cross(b-a,c-a) / abs(b-a)))

#点cと線分abとの距離
def distance_p_ls(a,b,c):
    if dot(b-a,c-a) < EPS:
        return abs(c-a)
    elif dot(a-b,c-b) < EPS:
        return abs(c-b)
    else:
        return distance_p_l(a,b,c)

#線分a1a2と線分b1b2の交差判定
def is_intersected_ls(a1,a2,b1,b2):
    return ( cross(a2-a1,b1-a1) * cross(a2-a1,b2-a1) < EPS and cross(b2-b1,a1-b1) * cross(b2-b1,a2-b1) < EPS)

#線分a1a2と線分b1b2の交点計算
def intersection_ls(a1,a2,b1,b2):
    b = b2 - b1
    d1 = abs(cross(b,a1-b1))
    d2 = abs(cross(b,a2-b1))
    t = d1 / (d1 + d2)
    return (a1 + (a2-a1) * t)

#直線a1a2と直線b1b2の交点計算
def intersection_l(a1,a2,b1,b2):
    a = a2 - a1
    b = b2 - b1
    return (a1 + a * cross(b,b1-a1) / cross(b,a))
