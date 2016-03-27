import re
		
def Main():
	
	"""
	This function accepts a string with special characters in it, eg. an e-mail address,
	and then reverses (in place) the words in the string keeping the original position of 
	the	special characters 
	"""
	
	inputString = raw_input("Enter a string/email address : ")

	reversedWords = [ char[::-1] for char in re.findall('\w+', inputString, re.DOTALL) ]
	
	specialChars = [ spChar for spChar in re.findall('\W+', inputString, re.DOTALL) ]
	
	result = [None]*(len(reversedWords) + len(specialChars))
	
	result[::2] = reversedWords
	
	result[1::2] = specialChars

	print "Output :",
	print ''.join(element for element in result)
	
if __name__ == '__main__':
	Main()
