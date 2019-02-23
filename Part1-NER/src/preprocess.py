import nltk
import re


def tokenize_candidates(doc):
    """
    Tokenizes the string from a document into candidate tokens.
    Combines consecutive tokens of size 1, 2, 3 and 4 to create candidate tokens.
    :param doc: string, the text to be tokenized
    :return: list, the list of candidate tokens of length 1, 2, 3 and 4
    """
    tokens = nltk.word_tokenize(doc)
    #print(tokens)

    candidates = []
    for idx, token in zip(range(len(tokens)), tokens):
        # Add length one tokens
        candidates.append([get_prefix_token(tokens,idx), token, get_suffix_token(tokens,idx)])
        # Add length two tokens
        if idx - 1 >= 0:
            candidates.append([get_prefix_token(tokens,idx-1), tokens[idx - 1] + ' ' + token, get_suffix_token(tokens,idx)])
        # Add length two tokens
        if idx - 2 >= 0:
            candidates.append([get_prefix_token(tokens,idx-2), tokens[idx - 2] + ' ' + tokens[idx - 1] + ' ' + tokens[idx], get_suffix_token(tokens,idx)])
        # Add length two tokens
        if idx - 3 >= 0:
            candidates.append([get_prefix_token(tokens,idx-3), tokens[idx - 3] + ' ' + tokens[idx - 2] + ' ' + tokens[idx - 1] + ' ' + tokens[idx], get_suffix_token(tokens,idx)])

    return candidates

def get_prefix_token(tokens, index):
    if index == 0:
        return ''
    return tokens[index-1]

def get_suffix_token(tokens, index):
    if index == len(tokens)-1:
        return ''
    return tokens[index+1]

def convert_integer_file_number_to_string(file_number):
    if file_number <= 9:
        return "00" + str(file_number)
    elif file_number <= 99:
        return "0" + str(file_number)
    return str(file_number)


def get_document_string(file_type, file_number):
    if file_type == 'annotated':
        filename = '../dataset/' + convert_integer_file_number_to_string(file_number) + '.txt'
    elif file_type == 'raw':
        filename = '../raw-dataset/' + convert_integer_file_number_to_string(file_number) + '.txt'
    else:
        return ''

    with open(filename, 'r') as f:
        document_string = f.read()
    return document_string


def fetch_annotated_tokens(file_number):
    # Read all lines from the given file
    document_string = get_document_string('annotated', file_number)

    # Now, read line by line
    annotated_tokens = []
    # Find the positions of <loc> and </loc>
    start_positions = list(re.finditer('<loc>', document_string))
    end_positions = list(re.finditer('</loc>', document_string))
    for i in range(0, len(start_positions)):
        # Extract out the part between <loc> and </loc>
        annotated_tokens.append(document_string[start_positions[i].end():end_positions[i].start()])
    return annotated_tokens


def main():
    # Test API
    annotated_tokens = fetch_annotated_tokens(113)
    print(annotated_tokens)

    print('Testing tokenize_candidates()')
    print(tokenize_candidates(get_document_string('raw', 113)))


if __name__ == "__main__":
    main()
