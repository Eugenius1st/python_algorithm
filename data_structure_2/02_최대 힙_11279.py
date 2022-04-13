import sys
sys.stdin = open("input.txt", "rt")
import heapq as hq
def input():
    return sys.stdin.readline().rstrip()

N = int(input())

result = []
for i in range(N):
    num = int(input())
    if num == 0:
        if len(result)==0:
            print(0)
        else:
            res = hq.heappop(result)
            print(res * (-1))

    else:
        hq.heappush(result, num*(-1))