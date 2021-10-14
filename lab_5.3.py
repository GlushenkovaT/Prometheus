#~ def file_search(a, b):
	#~ s=a[0]+"/"
	#~ for i in a:
		#~ if isinstance(i, str):
			#~ if i == b:
				#~ return(i+b)
		#~ elif isinstance(i, list)== True:
			#~ if len(i) > 1:
				#~ recursion=file_search(i, b)
				#~ if s != None:
					#~ s = s + recursion
					#~ return(s)
#~ def file_search(folder, filename):
    #~ if isinstance(folder, list):
        #~ path = ''
        #~ for item in folder:
            #~ if isinstance(item, list):
                #~ if filename in item:
                    #~ path = folder[0] + '/' + filename
                #~ else: print 'False'
            #~ else: file_search(item, path)
        #~ print path
        #~ return path
    #~ else:
        #~ path = folder + '/' + filename
        #~ return path

print file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt')
print file_search([ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py'], 'find.me')
print file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py')

#~ def file_search(a, b):
	#~ s=a[0]+"/"
	#~ if b in a:
		#~ return(s+b)
	#~ if len(a) > 1:
		#~ for i in a:
			#~ if isinstance(i, list):
				#~ recursion = file_search(i, b)
				#~ if recursion != None:
					#~ s = s + recursion
					#~ return(s)

def file_search(folder, filename):
	try:
		s=folder[0]+"/"
		if filename in folder:
			return(s+filename)
		for i in folder:
			if isinstance(i, list)== True:
				if len(i) > 1:
					recursion=file_search(i, filename)
					if s != None:
						s = s + recursion
					return(s)
		return False
	except TypeError:
		return False


print file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt'), '-->C:/ideas.txt'
print file_search([ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py'], '-->find.me'), "-->False"
print file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py'), '-->/home/user2/desktop/new folder/hereiam.py'
print file_search(['C:'], 'crack.exe'), "-->False"
print file_search(['C:', '1.txt', '2.txt', '3.txt', '4.txt'], '4.txt'),"-->C:/4.txt"
print file_search(['C:', '1.txt', '2.txt', '3.txt', '4.txt'], '1.txt') ,"-->C:/1.txt"
print file_search(['D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me']], 'hey.py'], 'find.me'), "-->D:/tmp/new folder1/find.me"
print file_search(['/tmp', ['1', ['2', ['3', ['4', ['5', 'key1', 'key2', 'key3']]]]]], 'key3'), "-->/tmp/1/2/3/4/5/key3"