def text_analyser(text=None):
	"""Analyses your text"""
	if text == None:
		text = input("What is the text to analyse?\n")
	import string
	words = 0
	upper = 0
	lower = 0
	punc = 0
	space = 0
	for char in str(text):
		words += 1
		if char.isupper():
			upper += 1
		if char.islower():
			lower += 1
		if char in string.punctuation:
			punc += 1
		if char == ' ':
			space += 1
	if words == 0:
		print("The text is empty")
	else:
		print("The text contains",  words, "characters:")
		print("- ", upper, "upper letters")
		print("- ", lower, "lower letters")
		print("- ", punc, "punctuation marks")
		print("- ", space, "spaces")
