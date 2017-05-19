def Eps(str1,str2):
    '''
    checks if str1 is in str2
    returns -1 means str1 not in str2
    '''
    try:
        str2.index(str1)
    except Exception:
        return -1
    return str2.index(str1)

def gcomposition(graph1,graph2):
    ### composes graph 1 with graph 2 by following arrows and returns a graph
    #g2dom = []
    ANS= []
    #for y in graph2:
    #    g2dom.append(y[0])
    for x in graph1:
        #print(x[1],Eps(x[1],g2dom))
        #if Eps(x[1],g2dom) > -1:
        for y in graph2:
            if y[0] == x[1]:
                ANS.append([x[0],y[1]])
    return ANS
G1 = [[1,2],["A","B"],[[3,4],[5,6]],[7,["yuku yo"]],["so transiently","Kotoko"]]
G2 = [["subversively",[1,5]],[[1,2],[1,2]],["B","D"],["B","F"],["Kotoko","works with strings"],[9,10],[11,5],["Dwarf fortress","wtf"]]
#print(gcomposition(G1,G2))

