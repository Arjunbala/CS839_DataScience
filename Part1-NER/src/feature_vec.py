import io
import numpy as np

# Everything else is garbage prefix
possible_location_prefixes = ['at', 'in', 'of', 'the', 'to', 'across']   # case?

# Everything else is garbage suffix
possible_location_suffixes = ['based']


# Get word vectors from vocabulary (glove, word2vec, fasttext ..)
def get_wordvec(path_to_vec):
    word_vec = {}

    with io.open(path_to_vec, 'r', encoding='utf-8') as f:
        # if word2vec or fasttext file : skip first line "next(f)"
        for line in f:
            word, vec = line.split(' ', 1)
            word_vec[word] = np.fromstring(vec, sep=' ')

    return word_vec

word_vecs = get_wordvec('glove.6B.50d.txt')


def get_feature_vec(candidate):
    """

    :param candidate:
    :return:
    """
    features = np.zeros(58)
    count = 0
    for tok in candidate[1].split():
        if tok.lower() in word_vecs:
            features[0:50] = np.add(features[0:50], word_vecs[tok.lower()])
            count += 1
    if count > 0:
        features = features / count
    else:
        features = np.zeros(58)
    features[50] = is_capitalized(candidate)
    features[51] = get_prefix_class(candidate)
    features[52:54] = get_number_of_tokens(candidate)
    features[54] = get_suffix_class(candidate)
    features[55] = is_suffix_capital(candidate)
    features[56] = is_prefix_capital(candidate)
    features[57] = is_prob_name(candidate)
    return features

def is_prob_name(candidate):
    name_prob = ["Mr", "Mrs", "Ms", "Dr"]
    if candidate[0] in name_prob:
        return 1
    return 0

def is_prefix_capital(candidate):
    if candidate[0] == '':
        return 0
    if candidate[0][0].isupper():
        return 1
    return 0

def is_suffix_capital(candidate):
    if candidate[2] == '':
        return 0
    if candidate[2][0].isupper():
        return 1
    return 0


def is_capitalized(candidate):
    for i in range(len(candidate[1])):
        if not candidate[1][i][0].isupper():
            return 0
    return 1


def is_dictionary_word(candidate):
    pass


def get_number_of_tokens(candidate):
    length_of_candidate = len(candidate[1].split(' '))
    return list(np.eye(2)[length_of_candidate - 1])


def get_length_of_individual_tokens(candidates):
    pass


def get_prefix_class(candidate):
    if candidate[0] in possible_location_prefixes:
        return 1
    return 0


def get_suffix_class(candidate):
    if candidate[2] in possible_location_suffixes:
        return 1
    return 0


def get_part_of_speech(candidate):
    pass


def main():
    get_feature_vec(['', 'Hello India Walo', ''])


if __name__ == "__main__":
    main()

