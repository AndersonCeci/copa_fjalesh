import re
 
def fetch_all_words(text):
    """
    pay attention to the regex here, perhaps you need a different definition of a word.
    """
    return re.findall(r"[\w'-]+", text)
 
 
def word_has_uppercase(word):
    for letter in word:
        if letter.isupper():
            return True
 
    return False
 
def word_has_digits(word):
    for letter in word:
        if letter.isdigit():
            return True
 
    return False
 
def generate_ngrams(sentences_file, ngrams_file, n):
    """
    method to generate the ngrams
    :param sentences_file: refers to a file that has a sentence per line
    :param ngrams_file: refers to the file that will be created which will contain the relevant ngrams
    """
    all_ngrams = []
 
    # opens the original file for reading 
    with open(sentences_file, 'r') as reading_file:
        # reads every line on the sentences_file
        lines = reading_file.readlines()
        ngrams = []
        for line in lines:
            # finds all the words on the file and saves them on the "words"
            words = fetch_all_words(line)
            for i in range(len(words) - n + 1):
                ngram = ' '.join(words[i: i + n]) + '\n'
 
                if word_has_uppercase(ngram) or word_has_digits(ngram):
                    continue
 
                ngrams.append(ngram)
 
        all_ngrams.extend(ngrams)
 
 
    # opens the ngrams_file
    with open(ngrams_file, "w") as writing_file:
        writing_file.writelines(all_ngrams)
