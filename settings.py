# -*- coding: utf-8 -*-

import os
import nltk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

project_directory = BASE_DIR + '/projects_text/'

nltk.data.path.append(BASE_DIR + '/nltk_data/')

againsts = ['refuse', 'oppose', 'contre', 'rompre', 'combat', 'sorti', 'expuls']
fors = ['defend', 'accept', 'retrouv', 'adopt', 'favorable', 'sauve']

subjects = {
    'libre-échange' : ['libre-echang', 'mondialis', 'TAFTA', 'CETA'],
    'souveraineté' : ['souverainete', 'sortie de l\'union européenne', 'frontière'],
    'immigration' : ['immigr'],
    'terrorisme' : ['terroris', 'extremis', 'attentat'],
    'ecologie' : ['environnement', 'ecolo', 'energies renouvelable', 'energies nouvelle'],
    'europe' : ['union europeenne', 'europe', 'euro'],
}

candidates = [       
    { 'name': "Nathalie Arthaud", 'file': 'arthaud.txt'},
    { 'name': "Philippe Poutou", 'file': 'poutou.txt'},
    { 'name': "Jean-Luc Mélenchon", 'file': 'melenchon.txt'},
    { 'name': "Jacques Cheminade", 'file': 'cheminade.txt'},
    { 'name': "Benoît Hamon", 'file': 'hamon.txt'},
    { 'name': "Emmanuel Macron", 'file': 'macron.txt'},
    { 'name': "Jean Lassalle", 'file': 'lassalle.txt'},
    { 'name': "François Fillon", 'file': 'fillon.txt'},
    { 'name': "Nicolas Dupont-Aignan", 'file': 'nda.txt'},
    { 'name': "François Asselineau", 'file': 'asselineau.txt'},
    { 'name': "Marine Le Pen", 'file': 'le-pen.txt'},
]
