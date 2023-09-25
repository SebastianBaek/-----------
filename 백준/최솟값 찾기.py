# https://www.acmicpc.net/problem/11003
from heapq import heappush, heappop
import sys

N, L = map(int, input().split())
numbers = list(map(int, sys.stdin.readline().split()))

heap = []
ans = []
for i in range(L):
    heappush(heap, (numbers[i], i))
    print(heap[0][0], end=" ")

for i in range(L, N):
    while (heap[0][1] <= i - L):
        heappop(heap)

    heappush(heap, (numbers[i], i))
    print(heap[0][0], end=" ")
