#!bin/python
# -*- coding: utf-8 -*-

from settings import *
import nltk
import sys
import textract
import re
import unicodedata

def parse_project(filename):
    text = textract.process(project_directory + filename)
    text = text.decode('utf-8')
    text = text.strip().lower()
    return text

if __name__ == '__main__':
    print("Analyse des programmes...\n\n")
    
    for candidate in candidates.values():
        candidate['opinions'] = {}        
        text = parse_project(candidate.get('file'))
        sentences = nltk.sent_tokenize(text, 'french')
        for sentence in sentences:
            tokens = nltk.word_tokenize(sentence, 'french')
            for token in tokens:
                t = unicodedata.normalize('NFD', token).encode('ascii', 'ignore')

                #Analyse sujet libre échange
                libre_echange = subjects['libre_echange']
                candidate['opinions']['libre-échange'] = {}
                candidate['opinions']['libre-échange']['total'] = 0
                candidate['opinions']['libre-échange']['against'] = 0
                candidate['opinions']['libre-échange']['for'] = 0
                for word in libre_echange:                    
                    reg = re.compile(r".*" + word + ".*")
                    if re.search(reg, t.decode('utf-8')):                        
                        candidate['opinions']['libre-échange']['total'] += 1
                        print(candidate)
                        for token in tokens:
                            #Suppression des accents
                            t2 = unicodedata.normalize('NFD', token).encode('ascii', 'ignore')
                            for a in againsts:                                
                                reg = re.compile(r".*" + a + ".*")
                                if re.search(reg, t2.decode('utf-8')):                                   
                                    candidate['opinions']['libre-échange']['against'] += 1
                                    print(candidate)
                            for f in fors:                                
                                reg = re.compile(r".*" + f + ".*")
                                if re.search(reg, t2.decode('utf-8')):                                   
                                    candidate['opinions']['libre-échange']['for'] += 1
                                    print(candidate)
                                    
        print('\n'+candidate['name'])
        print("Phrases concernées : " + str(candidate['opinions']['libre-échange']['total']))
        print("Avis pour : " + str(candidate['opinions']['libre-échange']['for']))
        print("Avis contre : " + str(candidate['opinions']['libre-échange']['against']))
        print('\n\n')
