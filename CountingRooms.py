from collections import * 
from functools import *
import heapq 


# i/p 
# The first input line has two integers 
# �
# n and 
# �
# m: the height and width of the map.

# Then there are 
# �
# n lines of 
# �
# m characters describing the map. Each character is either . (floor) or # (wall). 

# what we do :
# start with floor visit all floor near by it . count number of connected components 
#one Way to do it is using BFS/DFS   

def dfs(i,j):
    
    if i<0 or i>=n or j>=m or j<0 or  grid[i][j] == "#" or grid[i][j] == 1: return;
    
    grid[i][j] = 1
    
    dfs(i+1,j) 
    dfs(i,j+1) 
    dfs(i-1,j) 
    dfs(i,j-1) 

def bfs(i,j):
    
    q = deque([(i,j)]) 
    
    while q:
        
        for _ in range(len(q)):
            
            r,c = q.popleft() 
            
            grid[r][c] = 1
            
            for dx , dy in [(-1,0) , (1,0) , (0,1) , (0,-1)]:
                
                x  = r + dx 
                y = c + dy 
                
                if 0 <= x < n and  0<= y < m and grid[x][y] == ".": 
                    q.append((x,y)) 
                    
                    
                    
# Method 3 Disjoit Set (Union Find) 

class UF:
    
    def __init__(self , n): 
        
        self.rank = defaultdict(int) 
        self.parent = [i for i in range(n)] 
        
    def Union(self, u , v): 
        
        pu ,  pv = self.find(u) , self.find(v)   
        
        if pu == pv: return True 
        
        if self.rank[pu] > self.rank[pv]: 
            
            self.parent[pv] = pu 
            self.rank[pu] += self.rank[pv] 
        
        elif self.rank[pu] < self.rank[pv]: 
            
            self.parent[pu] = pv 
            self.rank[pv] += self.rank[pu] 
        
        else: 
            
            self.rank[pu] += 1 
            self.parent[pv] = pu 
            
        return True
        
        
    
    def find(self,u):
        
        if self.parent[u] == u: return u; 
        
        self.parent[u] = self.find(self.parent[u]) 
        
        return self.parent[u]
                    
                    
                    

    
    
def CountingRooms(grid,n,m):  
    
    # provide each [i,j] some ids 
    d  = defaultdict(int) 
    
    idx = 0 
    
    for i in range(n):
        
        for j in range(m): 
            
            if grid[i][j] == ".":
                
                d[i,j] = idx
                idx += 1  
    
    uf = UF(idx)
    
    for i in range(n):
        
        for j in range(m):
            
            if grid[i][j] == ".":
                
               # left  i-1
                if i > 0 and grid[i-1][j] == ".": 
                    uf.Union( d[i,j] , d[i-1 , j]) 
                # right i+1 
                if i < n-1 and grid[i+1][j] == ".": 
                    uf.Union(d[i,j] , d[i-1 , j])  
                    
                # down j+1 
                if j < m-1 and grid[i][j+1] == ".": 
                    uf.Union(d[i,j] , d[i,j+1]) 
                    
                # up j-1
                if j > 0 and grid[i][j-1] == ".": 
                    uf.Union(d[i,j] , d[i , j-1]) 
 
    # print(uf.parent)
    return len(set(uf.parent))
                
    
    
    
    
    

# ip 

n,m = map(int,input().split()) 
grid = [] 
for _ in range(n):
    ins = input()
    grid.append([i for i in ins])  

    
print(CountingRooms(grid,n,m))
