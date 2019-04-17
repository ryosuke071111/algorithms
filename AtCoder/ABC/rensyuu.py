from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
ls=["a","b","c","d"]
print(list(permutations(ls,2)))
print(list(combinations(ls,2)))
print(list(combinations_with_replacement(ls,2)))
