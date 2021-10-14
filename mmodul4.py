import sys
import math

text = " I canT DAnCE i CANt TAlK Hey"
key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

#удаляем пробелы
text = text.split()
text = ''.join(text)

#разбиваем тест на группы
for x in range(0, len(text), 5) :
		if range(x) < 5:
			del l[l.index(x)]
		print(text[x:x+5])
