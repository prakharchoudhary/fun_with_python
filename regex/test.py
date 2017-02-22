def check(string):
	s = []
	s[:] = [0]*256 
	for i in string:
		s[ord(i)] +=1
	i=0
	count=0
	while(i<256):
		if(s[i] == 1):
			count += 1
			print s[i], chr(i)
		i += 1
	return count

string = raw_input()
print check(string)