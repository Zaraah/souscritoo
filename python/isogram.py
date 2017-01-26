def is_isogram(string):
	liste = []
	for letter in string :
		print letter
		if letter in liste :
			print("false")
			return 0
		else :
			liste.append(letter)
	print("true")
	return 0


is_isogram("coucou")
is_isogram("dermatoglyphics")
