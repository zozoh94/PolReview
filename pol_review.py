#!bin/python
# -*- coding: utf-8 -*-

from settings import *
import nltk
import sys
import textract
import re

def parse_project(filename):
    text = textract.process(project_directory + filename)
    text = text.decode('utf-8')
    return text
        
if __name__ == '__main__':
    for candidate in candidates.values():
        text = parse_project(candidate.get('file'))
        text = nltk.word_tokenize(text, 'french')
        print(text)
