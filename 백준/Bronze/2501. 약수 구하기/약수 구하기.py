# 두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.
import sys
N, K = map(int, sys.stdin.readline().split())

lists = [i for i in range(1, N+1) if N%i==0]
length_list = len(lists)
if K>length_list:
    print(0)
else:
    print(lists[K-1])
