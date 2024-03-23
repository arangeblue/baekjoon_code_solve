import sys
from collections import deque
import copy
from itertools import combinations

n, m = list(map(int, input().split()))
graph = [list(map(int, input().split())) for i in range(n)]

# 0인 영역의 좌표
empty_coor = [(i,j) for i in range(n) for j in range(m) if graph[i][j] == 0 ] 

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
wall_num = 3
result = 0
# 3개인 0 좌표의 조합쌍에서 하나씩 꺼내어 벽을 만든 후 바이러스를 퍼뜨리고 0의 영역을 count
for combi_coor in combinations(empty_coor, wall_num):
    
    temp_graph = copy.deepcopy(graph)
    
    for wx,wy in combi_coor:
        temp_graph[wx][wy] = 1
        
    virus_q = deque([(i,j) for i in range(n) for j in range(m) if graph[i][j] == 2 ])
    
    while virus_q:
        
        x, y = virus_q.popleft()
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if temp_graph[nx][ny] == 0:
                    temp_graph[nx][ny] = 2
                    virus_q.append((nx,ny))
                    
    
    cnt = 0
    
    for row in temp_graph:
        cnt += row.count(0)
    
    result = max(result, cnt)
    
print(result)
    
    
    
    
     
    
    