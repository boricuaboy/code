text = str(raw_input("Enter a sentence: "))

def reverse_words(text):
	answer = ''
	temp = ''
	for char in text:
		if char != ' ':
			temp += char
		else:
			answer = temp + ' ' + answer
			temp = ''
	answer = temp + ' ' + answer
	return answer
	
print reverse_words(text)