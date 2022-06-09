import io
import sys

_INPUT = """\
6
4 7
1 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S,T=map(int,input().split())
  print(T-S+1)