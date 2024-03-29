import sys

def input():
    return sys.stdin.readline().rstrip()

def GCD(x,y):
    if y == 0:
        return x
    else:
        return GCD(y, x%y)

N = int(input())
A = list(map(int, input().split()))
X = int(input())
ans = []
for i in A:
    if GCD(X,i) == 1:
        ans.append(i)
print(sum(ans)/len(ans))