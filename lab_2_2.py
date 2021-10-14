import sys
import math

text = "Everybody sing a song:"
la = "la-la"

y = input ( "Введи число:")

if int(y) == "1" :
	print (text + la*int(y) + ".")
elif int(y) == "0" :
	print (text + "!")
elif int(y) > 1 :
	print (text + la*int(y) + ".")
else :
	print ('.')
