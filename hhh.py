input_list = [[32, 32.1, 32.0, -123]]
def clean_list(l):
	output_list = []
	for i in l:
		typ=type(i)
		if i not in output_list:
			output_list.append(i)
		if i in output_list:
			if type(i) != type(output_list[output_list.index(i)]):
				output_list.append(typ(i))
	return(output_list)

print (clean_list(input_list))