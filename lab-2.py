import sys, math;

x=0.3
n=0.4
q=0.5

y1=(1 / (q * math.sqrt(2 * math.pi)));
y2=math.exp( - ((x - n)**2) / (2*(q**2)));

print(y1*y2)