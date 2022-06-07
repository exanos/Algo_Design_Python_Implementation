graph={
'a':['b','c','v'],
'b':['e','f','k','s'],
'c':['f','i','w'],
'd':['f','g','o'],
'e':['d','l','o'],
'f':['j','n','t'],
'g':['n','o','x'],
'h':['a','e','o'],
'i':['l','m','t'],
'j':['k','n','m'],
'k':['c','j','m','w'],
'l':['b','o','p','x'],
'm':['d','j','y','u'],
'n':['g','i','k'],
'o':['d','h','x'],
'p':['q','u','z'],
'q':['x','l','s'],
'r':['m','y','i'],
's':['q','b','p','v'],
't':['j','r','w'],
'u':['l','p','z','m'],
'v':['a','s','y'],
'w':['h','k','t'],
'x':['g','l','s'],
'y':['z','r','v'],
'z':['u','m','y']
}

path=[]#format: ['a','b','f','n','i','m']
ini='d'
fin='z'


def DFS(graph,ini,fin):
    Discovered=[]
    stack=[ini]
    Tree=[]
    while len(stack)>=0:
        try:
            u=stack.pop()
        except:
            break
        if u not in Discovered:
            Discovered.append(u)
            for v in graph[u]:
                if v not in Discovered:
                    stack.append(v)
                    Tree.append([u,v])
                    if v==fin:
                        path=Path(Tree,ini,fin)
    return Tree, path
def BFS(graph,ini,fin):
    Discovered=[ini]
    L=[[ini]]
    Tree=[]
    i=0
    lv=L[i]
    while lv:
        try:
            lv=L[i]
        except IndexError:
            break
        l=[]
        for u in lv:
            for v in graph[u]:
                if v not in Discovered:
                    Discovered.append(v)
                    l.append(v)
                    Tree.append([u,v])
                    if v==fin:
                        path=Path(Tree,ini,fin)
                        
        L.append(l)
        i+=1
    return Tree, path
def Path(Tree,ini,fin):
    path=[]
    fin1=fin
    lng=len(Tree)-1
    i=0
    lv=1
    while fin1!=ini:
        u=Tree[i][1]
        if u==fin1:
            fin1=Tree[i][0]
            path.append(u)
        if i>=lng:
            lv=-1
        elif i<=0:
            lv=+1
        i+=lv*1
    path.reverse()
    return path

def longestpath(graph):
    iter=0
    maxi=0
    maxl=[]
    imax,jmax='',''
    for i in graph:
        for j in graph:
            if i!=j:
                Tree, path=BFS(graph,i,j)
                if len(path)>maxi:
                    maxi=len(path)
                    maxpath=path
                    imax=i
                    jmax=j
                    maxl.append([imax,jmax,maxpath])
            Tree,path=[],[]
            iter+=1
    print('iterations:',iter)
    return maxi, maxl


Tree,path=BFS(graph,ini,fin)
print('Tree:',Tree)
print('Path:',path)


