import numpy as np

# Everything else is garbage prefix
possible_location_prefixes = ['at', 'in', 'of', 'the']   # case?

# Everything else is garbage suffix
possible_location_suffixes = ['based']


def get_feature_vec(candidate):
    """

    :param candidate:
    :return:
    """
    features = []
    features.append(is_capitalized(candidate))
    features.extend(get_number_of_tokens(candidate))
    features.append(get_prefix_class(candidate))
    features.append(get_suffix_class(candidate))
    # print(features)
    return np.asarray(features)


def is_capitalized(candidate):
    for i in range(len(candidate[1])):
        if not candidate[1][i][0].isupper():
            return 0
    return 1


def is_dictionary_word(candidate):
    pass


def get_number_of_tokens(candidate):
    length_of_candidate = len(candidate[1].split(' '))
    return list(np.eye(4)[length_of_candidate - 1])


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
