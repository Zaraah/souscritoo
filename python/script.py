
def my_function(string):
	i = 0
	newLetter = 'a'
	newText = 'a'
	for letter in string:
		if i%2 == 0 :
			newLetter=letter
		else :
			newLetter=letter.upper()
		print newLetter 
		newText += newLetter
		i += 1
	return 0

my_function("bonjour")
