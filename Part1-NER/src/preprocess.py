import nltk
import re
import numpy as np
from feature_vec import get_feature_vec


def should_drop_candidate(candidate):
    stopwords = ["the", "a", "an", "i", "is", "if", "he", "her", "my","mr","mr.","mrs","mrs.","dr","dr."]
    # First letter of every word should be capital
    words = candidate[1].split(' ')
    if words[0].lower() in stopwords:
        return True
    for word in words:
        if not word[0].isupper():
            return True
    return False


def label_dataset(file_list):
    """
    For each word, labels it as 1 if it is a location, else 0. Also transforms the word to its feature vector
    :return: DataFrame, 1st column: feature vector of the word, 2nd column: label indicating location or not
    """
    X = []
    y = []
    for filenum in file_list:
        # print(filenum)
        doc_str = get_document_string('raw', filenum)
        candidates = tokenize_candidates(doc_str)
        annotated_tokens = fetch_annotated_tokens(filenum)
        for candidate in candidates:
            # Preprocessing
            if should_drop_candidate(candidate):
                continue
            X.append(get_feature_vec(candidate))
            # X.append(candidate[1])
            if candidate[1] in annotated_tokens:
                y.append(1)
            else:
                y.append(0)
    return np.asarray(X), np.asarray(y)


def tokenize_candidates(doc):
    """
    Tokenizes the string from a document into candidate tokens.
    Combines consecutive tokens of size 1, 2, 3 and 4 to create candidate tokens.
    :param doc: string, the text to be tokenized
    :return: list, the list of candidate tokens of length 1, 2, 3 and 4
    """
    tokens = nltk.word_tokenize(doc)
    # print(tokens)

    candidates = []
    for idx, token in zip(range(len(tokens)), tokens):
        # Add length one tokens
        candidates.append([get_prefix_token(tokens, idx), token, get_suffix_token(tokens, idx)])
        # Add length two tokens
        if idx - 1 >= 0:
            candidates.append(
                [get_prefix_token(tokens, idx - 1), tokens[idx - 1] + ' ' + token, get_suffix_token(tokens, idx)])
        # Add length two tokens
        '''
        if idx - 2 >= 0:
            candidates.append(
                [get_prefix_token(tokens, idx - 2), tokens[idx - 2] + ' ' + tokens[idx - 1] + ' ' + tokens[idx],
                 get_suffix_token(tokens, idx)])
        # Add length two tokens
        if idx - 3 >= 0:
            candidates.append([get_prefix_token(tokens, idx - 3),
                               tokens[idx - 3] + ' ' + tokens[idx - 2] + ' ' + tokens[idx - 1] + ' ' + tokens[idx],
                               get_suffix_token(tokens, idx)])
        '''
    return candidates


def get_prefix_token(tokens, index):
    """

    :param tokens:
    :param index:
    :return:
    """
    if index == 0:
        return ''
    return tokens[index - 1]


def get_suffix_token(tokens, index):
    """

    :param tokens:
    :param index:
    :return:
    """
    if index == len(tokens) - 1:
        return ''
    return tokens[index + 1]


def convert_integer_file_number_to_string(file_number):
    """
    Transforms an integer into proper file name format, ex: 055.txt
    :param file_number: int, file number
    :return: string, 0 appended string of length 3 for the file name
    """
    return '{0:03d}'.format(file_number)


def get_document_string(file_type, file_number):
    """
    Reads the required annotated/raw file with file_number as its name into a string.
    :param file_type: string, 'annotated' if annotated file is desired. else 'raw'
    :param file_number: int, file number
    :return: string, the contents of the file
    """
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
    """
    Retrieves the location tokens based on the <loc></loc> tags from an annotated file
    :param file_number: int, file number
    :return: list, all the location tokens from the annotated file
    """
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


def get_file_numbers():
    filename = "shuffled_file_numbers.txt"
    entire_list = []
    with open(filename) as f:
        for line in f:
            content = line.strip()
            entire_list.append(int(content))
    return entire_list[0:200], entire_list[200:300]


def main():
    d, v = get_file_numbers()
    print(len(d))
    print(len(v))
    # dataset = label_dataset()
    # print(dataset[dataset['y'] == 1])

    # Test API
    # annotated_tokens = fetch_annotated_tokens(113)
    # print(annotated_tokens)
    #
    # print('Testing tokenize_candidates()')
    # print(tokenize_candidates(get_document_string('raw', 113)))


if __name__ == "__main__":
    main()
