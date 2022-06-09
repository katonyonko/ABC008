import io
import sys

_INPUT = """\
6
4
taro
jiro
taro
saburo
1
takahashikun
9
a
b
c
c
b
c
b
d
e
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import defaultdict
  N=int(input())
  d=defaultdict(int)
  for i in range(N):
    d[input()]+=1
  m=max([d[k] for k in d])
  for k in d:
    if d[k]==m: print(k); break