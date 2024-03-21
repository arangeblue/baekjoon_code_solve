import sys
from collections import deque

input = sys.stdin.readline


dx = [1, -1, 1, -1, 2, -2, 2, -2]
dy = [2, 2, -2, -2, 1, 1, -1, -1] 

def bfs(sx, sy):
    q = deque([])
    q.append((sx, sy))
    graph[sx][sy] += 1
    
    while q:
        sx, sy = q.popleft()
        
        if sx == end_x and sy == end_y:
            return graph[sx][sy]
        
        for i in range(8):
            nx = sx + dx[i]
            ny = sy + dy[i]
            
            
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == -1:
                q.append((nx,ny))
                graph[nx][ny] = graph[sx][sy] + 1
            
    
C = int(input())
for _ in range(C):
    n = int(input())
    graph = [[-1] * n for _ in range(n)]
    start_x, start_y = map(int,input().split())
    end_x, end_y = map(int, input().split())
    result = bfs(start_x, start_y)
    print(result)