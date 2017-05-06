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
        if self.total < (self.fore + self.against):
            self.total = self.fore + self.against
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
    sentences = candidate['sentences']
    for sentence in sentences:
        for token in sentence:
            t = unicodedata.normalize('NFD', token).encode('ascii', 'ignore')

            libre_echange = subjects[subject]               
            for word in words_subjects:                    
                reg = re.compile(r".*" + word + ".*")
                if re.search(reg, t.decode('utf-8')):                        
                    candidate['opinions'][subject].total += 1
                    for token in sentence:
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

    
def tokenize_project(candidate):
    sentences = nltk.sent_tokenize(candidate['project'], 'french')
    tokens = []
    for sentence in sentences:
        tokens.append(nltk.word_tokenize(sentence, 'french'))
    return tokens
    
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
        if(opinion.ratio_for>opinion.ratio_against):
            print("Pour")
        elif(opinion.ratio_against>opinion.ratio_for):
            print("Contre")
        else:
            print("Neutre")
        
    print('\n\n')


if __name__ == '__main__':
    print("Analyse des programmes...\n\n")

    
    for candidate in candidates:
        candidate['project'] = parse_project(candidate.get('file'))
        candidate['sentences'] = tokenize_project(candidate)
        
        for subject in subjects:
            analyze_subject(candidate, subject)            
        
        print_results(candidate)

    subject = input("How about you choose a subject now : ")
    subjects[subject] = []
    key = input("key words for this subject(separated by ',') : ")
    subjects[subject] = key.split(',')
    for candidate in candidates:
        analyze_subject(candidate, subject)
        print_results(candidate)
