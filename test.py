#!bin/python
# -*- coding: utf-8 -*-

from settings import *
import nltk
import sys

if __name__ == '__main__':
    filename = BASE_DIR + '/test.txt'
    tokens = []
    with open(filename, 'r') as file:
        for line in file:
            tokens.extend(nltk.word_tokenize(line, 'french'))
    print(tokens)
    
