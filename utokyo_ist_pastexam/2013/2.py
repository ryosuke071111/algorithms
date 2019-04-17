# #8:54
# import itertools

# logic=input()
# alphabet=set([])
# kigou=["&","+"]

# for i in logic:
#   if i not in kigou and i not in alphabet:
#     alphabet.add(i)

# alphabet=list(alphabet)
# print(alphabet)

# ans=[]

# for i in itertools.product(range(2),repeat=len(alphabet)):
#   if eval(logic.replace(alphabet[0],str(i[0])).replace(alphabet[1],str(i[1])).replace(alphabet[2],str(i[2])))==True:
#         ans.append(i)

def PolandRev( formula ):
    formula_list = formula.split(" ") # スペース区切りで計算式をリストへ．
    opperands = ["+", "&", "_", "(", ")"]
    priority = { "(" : 20, ")" : 20, "_" : 10, "&" : 5, "+" : 0}
    stack = [] # オペランドを一時的に入れる
    buffer = [] # 完成した式をいれる
    checked = False

    for token in formula_list:
        if token in opperands:
            # オペランドである
            if token == opperands[3]: # "("
                stack.append( token )
            elif token == opperands[4]: # ")"
                for i in reversed( range( len( stack ) ) ):
                    if stack[i] == "(":
                        stack.pop(i)
                        break
                    else :
                        buffer.append( stack.pop(i) )
                if checked and stack[len(stack) - 1] == "_":
                    buffer.append( stack.pop() )
                    checked = False
            elif token == opperands[2]: # _
                checked = True
                stack.append( token )
            else : # _ or * or +
                while(1):
                    try :
                        lead = priority[ stack[len(stack)-1] ]
                    except :
                        lead = -1
                    if lead == -1 or priority[token] > lead or lead == 20:
                        stack.append( token )
                        break
                    else :
                        buffer.append( stack.pop(len(stack)-1) )

        else :
            # オペランドでない，値である
            buffer.append( token )
            if checked and stack[len(stack) - 1] == "_":
                buffer.append( stack.pop() )
                checked = False

    for i in reversed( range( len( stack ) ) ):
        buffer.append( stack.pop(i) )
    print( "逆ポーランド記法 :" , end=" ")
    print( buffer )
    return buffer

def PolandCalc( formula, input=-1):
    count = 0
    stack = []
    variables = {}
    tmp = []
    opperands = ["+", "&", "_"]
    for token in formula:
        if token not in opperands and token not in variables:
            variables[token] = count
            count += 1
    if input == -1:
        input = makeList( count )
    for dataset in input:
        for token in formula:
            if token == opperands[0]: # +
                x = stack.pop(0)
                y = stack.pop(0)
                stack.insert( 0, x or y )
            elif token == opperands[1]: # *
                x = stack.pop(0)
                y = stack.pop(0)
                stack.insert( 0, x and y )
            elif token == opperands[2]: # _
                x = stack.pop(0)
                if x == 0:
                    y = 1
                else :
                    y = 0
                stack.insert( 0, y )
            else :
                stack.insert( 0, dataset[ variables[token] ] )
        tmp.append( stack[0] )
        stack = []
    tmp2 = [*variables.keys()]
    tmp2.append("F")
    input.insert( 0, tmp2 )
    for i in range( len( tmp ) ):
        input[ 1 + i ].append( tmp[i] )
    printInfo( input )
    return input

def makeList( key ):
    returnList = []
    pad = "{:0=" + str(key) + "}"
    for i in range(2 ** key):
        ｔｍｐ = format(i, "b")
        returnList.append( [*pad.format( int(tmp) )] )
        returnList[i] = [ int(x) for x in returnList[i] ]
    return returnList

def printInfo( dataset ):
    count = 0
    for i in range( len( dataset[0] ) ):
        print( dataset[0][i], end="\t" )
    print("")
    for set in dataset:
        count += 1
        if count == 1:
            continue
        for value in set:
            print( str(value), end="\t" )
        print("")

a=input()
a_s=""
for i in a:
  a_s+=i
  a_s+=" "
a_s=a_s[:-1]
print(a_s)
PolandCalc(PolandRev(a_s))
