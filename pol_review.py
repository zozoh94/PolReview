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
        self.no_opinions = 0
        self.ratio_for = 0
        self.ratio_against = 0
        self.ratio_no_opinions = 0        
        
    def finalize(self):        
        if self.fore > self.total:
            self.fore = self.total        
        if self.against > self.total:
            self.against = self.total
        self.no_opinions = self.total - self.fore - self.against
        if self.total != 0 and self.total != self.no_opinions:
            self.ratio_for = self.fore / (self.total-self.no_opinions)
            self.ratio_against = self.against / (self.total-self.no_opinions)

        
def parse_project(filename):
    text = textract.process(project_directory + filename)
    text = text.decode('utf-8')
    text = text.strip().lower()
    return text

def analyze_subject(candidate, subject):
    words_subjects = subjects.get(subject, None)
    if not words_subjects:
        print("Subject " + subject + " does not exist") 
        exit()
    if not candidate.get('opinions', None):
        candidate['opinions'] = {}          
    candidate['opinions'][subject] = Opinion(subject.title())
    text = parse_project(candidate.get('file'))
    sentences = nltk.sent_tokenize(text, 'french')
    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence, 'french')
        for token in tokens:
            t = unicodedata.normalize('NFD', token).encode('ascii', 'ignore')

            libre_echange = subjects[subject]               
            for word in words_subjects:                    
                reg = re.compile(r".*" + word + ".*")
                if re.search(reg, t.decode('utf-8')):                        
                    candidate['opinions'][subject].total += 1
                    candidate.update(opinions=candidate['opinions'])
                    for token in tokens:
                        #Suppression des accents
                        t2 = unicodedata.normalize('NFD', token).encode('ascii', 'ignore')
                        for a in againsts:                                
                            reg = re.compile(r".*" + a + ".*")
                            if re.search(reg, t2.decode('utf-8')):
                                candidate['opinions'][subject].against += 1
                        for f in fors:                                
                            reg = re.compile(r".*" + f + ".*")
                            if re.search(reg, t2.decode('utf-8')):                                   
                                candidate['opinions'][subject].fore += 1

    candidate['opinions'][subject].finalize()

def print_results(candidate):
    print('\n'+candidate['name'])

    for opinion in candidate['opinions'].values():        
        print("\n"+opinion.name+" :")
        print("Phrases concernées : " + str(opinion.total))
        print("Avis pour : " + str(opinion.fore))
        print("Avis contre : " + str(opinion.against))
        print("Sans avis : " + str(opinion.no_opinions))
        print("Indice pour : " + str(opinion.ratio_for))
        print("Indice contre : " + str(opinion.ratio_against))
        
    print('\n\n')


if __name__ == '__main__':
    print("Analyse des programmes...\n\n")
    
    for candidate in candidates:
        analyze_subject(candidate, 'libre-échange')
        analyze_subject(candidate, 'souveraineté')        
        
        print_results(candidate)
