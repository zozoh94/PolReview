#!bin/python
# -*- coding: utf-8 -*-

from settings import *
import nltk
import sys
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
    with open(project_directory + filename, "r") as filepointer:
        text = filepointer.read()
        text = text.strip().lower()
    return text
    
    
def subject(tokens, t,sujet):
    subject = subjects[sujet]               
    for word in subject:                    
        reg = re.compile(r".*" + word + ".*")
        if re.search(reg, t.decode('utf-8')):                        
            candidate['opinions'][sujet].total += 1
            candidate.update(opinions=candidate['opinions'])
            for token in tokens:
            #Suppression des accents
                t2 = unicodedata.normalize('NFD', token).encode('ascii', 'ignore')
                for a in againsts:                                
                    reg = re.compile(r".*" + a + ".*")
                    if re.search(reg, t2.decode('utf-8')):
                        candidate['opinions'][sujet].against += 1
                for f in fors:                                
                    reg = re.compile(r".*" + f + ".*")
                    if re.search(reg, t2.decode('utf-8')):                                   
                        candidate['opinions'][sujet].fore += 1

def analyze_candidates(candidate, sub):
    candidate['opinions'] = {}
    candidate['opinions'][sub] = Opinion(sub)
    text = parse_project(candidate.get('file'))
    sentences = nltk.sent_tokenize(text, 'french')
    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence, 'french')
        for token in tokens:
            t = unicodedata.normalize('NFD', token).encode('ascii', 'ignore')
            subject(tokens, t,sub)
    candidate['opinions'][sub].finalize()


def results(candidate):
    print('\n'+candidate['name'])
    for sub in subjects:
        print('\n'+sub+' :')
        print("Phrases concernées : " + str(candidate['opinions'][sub].total))
        print("Avis pour : " + str(candidate['opinions'][sub].fore))
        print("Avis contre : " + str(candidate['opinions'][sub].against))
        print("Sans avis : " + str(candidate['opinions'][sub].no_opinions))
        print("Indice pour : " + str(candidate['opinions'][sub].ratio_for))
        print("Indice contre : " + str(candidate['opinions'][sub].ratio_against))
        print('\n\n')

if __name__ == '__main__':
    print("Analyse des programmes...\n\n")
    for candidate in candidates:
        for sub in subjects:
            analyze_candidates(candidate,sub)
        results(candidate)
           
