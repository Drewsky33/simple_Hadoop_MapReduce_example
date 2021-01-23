#!/usr/bin/env python
import sys

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # make lower case
    line = line.lower()

    # split the line into words; splits on any whitespace
    words = line.split()

    # Import Scikit learns stop words

    from sklearn.feature_extraction import stop_words
    stops = set(stop_words.ENGLISH_STOP_WORDS)

    #remove punctuation

    import string
    s = "string. With. Punctuation?"
    out = s.translate(string.maketrans("",""), string.punctuation)

    # output tuples (word, 1) in tab-delimited format
    stopwords = set(['the', 'and'])

    for word in words:
        if word not in stopwords:
         print '%s\t%s' % (word, "1")
