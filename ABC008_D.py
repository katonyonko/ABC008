import io
import sys

_INPUT = """\
6
6 4
3
2 4
3 1
4 3
3 3
3
1 1
2 3
3 2
15 10
8
7 10
12 8
4 4
5 7
9 9
1 6
6 5
3 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  W,H=map(int,input().split())
  N=int(input())
  M=[]
  for i in range(N):
    X,Y=map(int,input().split())
    X-=1; Y-=1
    M.append((X,Y))
  memo={}
  def rec(r1,c1,r2,c2):
    if (r1,c1,r2,c2) in memo: return memo[(r1,c1,r2,c2)]
    internal=[M[i] for i in range(N) if r1<=M[i][0]<r2 and c1<=M[i][1]<c2]
    if len(internal)==0: return 0
    elif len(internal)==1: return r2-r1+c2-c1-1
    else:
      ans=0
      for i in range(len(internal)):
        x,y=internal[i]
        tmp=r2-r1+c2-c1-1
        if x>r1 and y>c1: tmp+=rec(r1,c1,x,y)
        if x>r1 and y<c2-1: tmp+=rec(r1,y+1,x,c2)
        if x<r2-1 and y>c1: tmp+=rec(x+1,c1,r2,y)
        if x<r2-1 and y<c2-1: tmp+=rec(x+1,y+1,r2,c2)
        ans=max(ans,tmp)
        memo[(r1,c1,r2,c2)]=ans
      return ans
  print(rec(0,0,W,H))