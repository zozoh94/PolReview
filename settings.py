# -*- coding: utf-8 -*-

import os
import nltk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

project_directory = BASE_DIR + '/projects/'

nltk.data.path.append(BASE_DIR + '/nltk_data/')

againsts = ['refuse', 'oppose', 'contre', 'rompre', 'combat']
fors = ['defend', 'accept']

subjects = {
    'libre_echange' : ['libre-echang', 'mondialis'],
}

<<<<<<< HEAD
candidates = [
    { 'name': "Nathalie Arthaud", 'file': 'arthaud.pdf'},
    { 'name': "Philippe Poutou", 'file': 'poutou.pdf'},
    { 'name': "Jean-Luc Mélenchon", 'file': 'melenchon.pdf'},
    { 'name': "Jacques Cheminade", 'file': 'cheminade.pdf'},
    { 'name': "Benoît Hamon", 'file': 'hamon.pdf'},
    { 'name': "Emmanuel Macron", 'file': 'macron.pdf'},
    { 'name': "Jean Lassalle", 'file': 'lassalle.pdf'},
    { 'name': "François Fillon", 'file': 'fillon.pdf'},
    { 'name': "Nicolas Dupont-Aignan", 'file': 'nda.pdf'},
    { 'name': "François Asselineau", 'file': 'asselineau.pdf'},
    { 'name': "Marine Le Pen", 'file': 'le-pen.pdf'},
]
=======
subject = {
    'eco' : { 'name' : "Economie", 'keywords': ['economie', 'liberalisme', 'protectionisme', 'banques', 'capitalisme', 'libre-échange', 'ficalité', 'compétitivité', 'dette', 'investissements', 'PME', 'TPE', 'dépenses', 'allocations', 'charges', 'impôts', 'coût', 'entreprises', '35 heures', 'chômage', 'bpifrance'] },
    
}
>>>>>>> b5670cee7f8b0cda05691f4d45e9beae64c0490e
