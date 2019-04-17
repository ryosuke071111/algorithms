lsx = [4, 100, 1, 5, 400,53, 54, 53432,5678, 13, 65, 6, 0, 32]

def bSort(a):
    for i in range(len(a)):
        for j in range(len(a)-1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
        print(i)

    return a

print(lsx)
bSort(lsx)
print(lsx)
