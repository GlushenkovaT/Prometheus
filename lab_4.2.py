import sys

a = sys.argv[1:]
a_list = list(reversed(a))    
new_a = " ".join(a_list)
print (new_a)