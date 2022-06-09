import io
import sys

_INPUT = """\
6
3
2
4
8
4
5
5
5
5
5
2
3
2
6
12
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  C=[int(input()) for _ in range(N)]
  C.sort()
  a=[0]*N
  for i in range(N):
    for j in range(N):
      if i!=j and C[j]%C[i]==0: a[j]+=1
  ans=0
  for i in range(N):
    ans+=(a[i]+2)//2/(a[i]+1)
  print(ans)