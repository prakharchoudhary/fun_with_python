import urllib

def read_text():
	quotes = open("")			#enter the location of document to be scanned for profanities
	contents = quotes.read()
	print contents
	quotes.close()
	check_profanity(contents)

def check_profanity(text_to_check):
	word_search = urllib.urlopen("http://www.wdylike.appspot.com/?q=shot" + text_to_check)		#"http://isithackday.com/arrpi.php?text=friend"----use this link to convert normal speech to pirate speech
	result = word_search.read()
	if result == "true":
		print "The document has profanities!!!!"
	elif result == "false":
		print "The document is clear and has no profanities."
	else:
		print "Can't scan the document"
	word_search.close()

read_text()