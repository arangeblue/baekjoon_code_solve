import heapq
import sys
input = sys.stdin.readline

n = int(input())

input_map = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j, m in enumerate(map(int, input().split())):
        input_map[i][j] = m
        
for k in range(n):
    for i in range(n):
        for j in range(n):
            if input_map[i][k] and input_map[k][j]:
                input_map[i][j] = 1
                
for i in range(n):
    for j in range(n):
        print(input_map[i][j], end=' ')
    print()