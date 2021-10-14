import sys

a = ''.join(a.split())
a = a.upper()
a = list(a)
b = list(reversed(a))
if a == b:
  print("YES")
else:
  print("NO")