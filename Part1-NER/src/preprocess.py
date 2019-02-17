import nltk


def tokenize_candidates(doc):
	"""
	Tokenizes the string from a document into candidate tokens.
	Combines consecutive tokens of size 1, 2, 3 and 4 to create candidate tokens.
	:param doc: string, the text to be tokenized
	:return: list, the list of candidate tokens of length 1, 2, 3 and 4
	"""
	tokens = nltk.word_tokenize(doc)
	print(tokens)

	candidates = []
	for idx, token in zip(range(len(tokens)), tokens):
		# Add length one tokens
		candidates.append(token)
		# Add length two tokens
		if idx - 1 >= 0:
			candidates.append(tokens[idx - 1] + ' ' + token)
		# Add length two tokens
		if idx - 2 >= 0:
			candidates.append(tokens[idx - 2] + ' ' + tokens[idx - 1] + ' ' + tokens[idx])
		# Add length two tokens
		if idx - 3 >= 0:
			candidates.append(tokens[idx - 3] + ' ' + tokens[idx - 2] + ' ' + tokens[idx - 1] + ' ' + tokens[idx])

	return candidates


def main():
	pass


if __name__ == "__main__":
	main()
