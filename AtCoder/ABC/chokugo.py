import re
s = input()

if re.match('^(ch|o|k|u)*$', s):
    print("YES")
else:
    print("NO")

