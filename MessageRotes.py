from collections import *  

# quite good bfs single source shortest path question very easy 
# tricky part is how efficiently you can retrieve path by creating a parent array of neighbhor elements
 
def solve(graph , n):
    
    q = deque([(1)])  
    
    # to retrieve the path we wiil store parents of childs  
    par = [-1]*(n+1)
    vis  = set() 
    
    while  q :
        
        for _ in range(len(q)):
            cur  = q.popleft() 
            vis.add(cur) 
            
            if cur == n: break
            for nei in graph[cur]:
                
                if nei not in vis : 
                    par[nei] = cur 
                    vis.add(nei)
                    q.append((nei)) 
    res = []  
    res.append(n)
    cur = n
    while par[cur]!=-1:
        cur = par[cur] 
        res.append(cur)
    return res[::-1]
 
 
 
n , m = map(int , input().split()) 
graph = defaultdict(list) 
for i in range(m):
    a , b = map(int , input().split()) 
    graph[a].append(b) 
    graph[b].append(a) 
    
res = solve(graph , n) 
print(len(res) if res!=[n] else "IMPOSSIBLE")
if res!=[n]:  
    print(*res) 
    
    
    
# this is the brute approach not efficient to retrieve path
# def solve(graph , n):
    
#     q = deque([(1 , 0 , -1 , [1])]) 
#     vis  = set() 
    
#     while  q :
        
#         for _ in range(len(q)):
#             cur , stp , par , path = q.popleft() 
#             vis.add(cur) 
            
#             if cur == n: return stp+1 , path
#             for nei in graph[cur]:
                
#                 if nei not in vis and nei!=par:
#                     q.append((nei , stp+1 , cur , path+[nei])) 
#     return -1