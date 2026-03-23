def add_prefix_un(word):
    return "un" + word


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = vocab_words[1:]

    # Apply prefix to each word
    prefixed_words = [prefix + word for word in words]

    # Join everything with ' :: '
    return " :: ".join([prefix] + prefixed_words)


def remove_suffix_ness(word):
    base = word[:-4]  # remove 'ness'

    # If word ends with 'i', convert to 'y'
    if base.endswith('i'):
        return base[:-1] + 'y'
    return base


def adjective_to_verb(sentence, index):
    words = sentence.split()

    # Remove punctuation if present
    word = words[index].strip('.,!')

    return word + "en"