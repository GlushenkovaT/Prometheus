import sys
str = sys.argv[1]

count = 0

for char in str:
    if char == ')':
        count -= 1
    elif count < 0:
        break
    elif char == '(':
        count += 1
        
if count == 0:
    print "YES"
else: 
    print "NO"