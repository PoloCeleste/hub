from heapq import heappop,heappush
import sys
N=int(sys.stdin.readline())
heap=[]
for n in range(N):
    x=int(sys.stdin.readline())
    if x==0:
        if heap:
            y=heappop(heap)
            print(y[0]*y[1])
        else:print(0)
    else:
        if x>0:
            heappush(heap, (abs(x), 1))
        else:
            heappush(heap, (abs(x), -1))