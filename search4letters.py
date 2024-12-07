def search4letters(phrase:str, letters:str='aeiou') -> set:
    return set(letters).intersection(set(phrase))
def result():
	output = {}
	output = set(search4letters(input('enter the phrase:\t')))
	print(output)
