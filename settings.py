# -*- coding: utf-8 -*-

import os
import nltk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

project_directory = BASE_DIR + '/projects/'

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
