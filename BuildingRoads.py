# Byteland has n
#  cities, and m
#  roads between them. The goal is to construct new roads so that there is a route between any two cities.

# Your task is to find out the minimum number of roads required, and also determine which roads should be built. 

# find no of connected components , let say 
# 1-2-3-4 
# 5-6-7 
# 8-9 
# need to connect these 3 cities i need 3 roads i connect 4-5 then 7-8 ; 

# One way Use dfs to count number of connected components  
# mark them visited or store them to some container 
#now roads will be the length of container - 1 and cities we are connecting will be i , i+1 for all i < n; 

# TestCase
# 9 7 
# 1 2 
# 2 3 
# 3 4 
# 4 1
# 5 6 
# 6 7 
# 8 9 


from collections import * 
# Using DFS
def solve(edges , n):
    
   
    
    graph = defaultdict(list) 
    
    for a,b in edges:
        graph[a].append(b) 
        graph[b].append(a) 
   
    def dfs(node , par):
       
        vis.add(node) 
        for ch in graph[node]:
            if ch not in vis:
                dfs(ch,node) 
    
    vis   , compo = set() , []
    for i in range(1,n+1):
        if i not in vis:
            compo.append(i) 
            dfs(i,-1) 
            
  
    print(len(compo)-1) 
    
    for i in range(len(compo)-1):
        print(compo[i] , compo[i+1])
     
    return; 

# Using DSU
def solve(edges , n):
    
    print(edges)
    
    rank = defaultdict(int) 
    parent = [i for i in range(n+1)]  

    def find(i):
        if i == parent[i]: return i 
        parent[i] = find(parent[i])
        return parent[i]

    def Union(a,b):
        par_a = find(a)  
        par_b = find(b)  

        if par_a == par_b: return False

        if rank[par_a]>rank[par_b]:
            parent[par_b] = par_a      
        elif rank[par_a]<rank[par_b]:
            parent[par_a] = par_b   
        else:
            parent[par_b] = par_a
            rank[par_a]+=1  
        return True 
    
    for a,b in edges:
        if find(a) != find(b):
            
            Union(a,b) 
    
    noOfComponents = list(set(parent)) 
    print(len(noOfComponents)-2)  
    
    for i in range(1,len(noOfComponents)-1):
        print(noOfComponents[i] , noOfComponents[i+1])
     
    return; 
    



NoOfCities , Roads = map(int,input().split())
edges = [] 
for i in range(Roads):
    a , b = map(int,input().split()) 
    edges.append([a,b]) 
solve(edges , NoOfCities)