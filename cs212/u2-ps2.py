import itertools
def floor_puzzle():
#    return [Hopper, Kay, Liskov, Perlis, Ritchie]
    return map(list, [e for e in itertools.permutations([1, 2, 3, 4, 5])
             if (e[0]!=5) and 
                (e[1]!=1) and 
                (e[2]!=1 and e[2]!=5) and
                (e[3]>e[1]) and 
                (e[4]!=e[2]+1 and e[4]!=e[2]-1) and
                (e[2]!=e[1]+1 and e[2]!=e[1]-1)
                ])
print floor_puzzle()
