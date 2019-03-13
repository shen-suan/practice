import sys

for s in sys.stdin:
    s=s[:-1]
    nums=s.split(' ')
    a, b=nums
    a, b=int(a), int(b)
    print(a+b)
