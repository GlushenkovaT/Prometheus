import sys
a1 = int(sys.argv[1])
a2 = int(sys.argv[2])
count = 0

for num in range(a1, a2+1):
	num = list(str(num))
	num0 = [0 for i in range(6 - len(num))]
	num = num0 + num	
		
	if (int(num[0]) + int(num[1]) + int(num [2])) == (int(num[3]) + int(num[4]) + int(num[5])):
		count += 1

print count