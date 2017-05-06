#!bin/python
# -*- coding: utf-8 -*-

from settings import *
import nltk
import sys
import textract
import re
import unicodedata


class Opinion:
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.fore = 0
        self.against = 0
        self.moy_pour=0
        self.moy_contre=0
        
def parse_project(filename):
    text = textract.process(project_directory + filename)
    text = text.decode('utf-8')
    text = text.strip().lower()
    return text

if __name__ == '__main__':
    print("Analyse des programmes...\n\n")
    
    for candidate in candidates:
        candidate['opinions'] = {}        
        candidate['opinions']['libre-échange'] = Opinion('libre-échange')
        text = parse_project(candidate.get('file'))
        sentences = nltk.sent_tokenize(text, 'french')
        for sentence in sentences:
            tokens = nltk.word_tokenize(sentence, 'french')
            for token in tokens:
                t = unicodedata.normalize('NFD', token).encode('ascii', 'ignore')

                #Analyse sujet libre échange
                libre_echange = subjects['libre_echange']               
                for word in libre_echange:                    
                    reg = re.compile(r".*" + word + ".*")
                    if re.search(reg, t.decode('utf-8')):                        
                        candidate['opinions']['libre-échange'].total += 1
                        candidate.update(opinions=candidate['opinions'])
                        for token in tokens:
                            #Suppression des accents
                            t2 = unicodedata.normalize('NFD', token).encode('ascii', 'ignore')
                            for a in againsts:                                
                                reg = re.compile(r".*" + a + ".*")
                                if re.search(reg, t2.decode('utf-8')):
                                    candidate['opinions']['libre-échange'].against += 1
                            for f in fors:                                
                                reg = re.compile(r".*" + f + ".*")
                                if re.search(reg, t2.decode('utf-8')):                                   
                                    candidate['opinions']['libre-échange'].fore += 1
        if( candidate['opinions']['libre-échange'].total != 0):
            candidate['opinions']['libre-échange'].moy_pour=candidate['opinions']['libre-échange'].fore / candidate['opinions']['libre-échange'].total
            candidate['opinions']['libre-échange'].moy_contre=candidate['opinions']['libre-échange'].against / candidate['opinions']['libre-échange'].total
        print('\n'+candidate['name'])
        print("\nLibre échange :")
        print("Phrases concernées : " + str(candidate['opinions']['libre-échange'].total))
        print("Avis pour : " + str(candidate['opinions']['libre-échange'].fore))
        print("Avis contre : " + str(candidate['opinions']['libre-échange'].against))
        print("indice pour : " + str(candidate['opinions']['libre-échange'].moy_pour))
        print("indice contre : " + str(candidate['opinions']['libre-échange'].moy_contre))
        print('\n\n')
