# -*- coding: utf-8 -*-

import os
import nltk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

project_directory = BASE_DIR + '/projects/'

nltk.data.path.append(BASE_DIR + '/nltk_data/')

candidates = {
    'arthaud': { 'name': "Nathalie Arthaud", 'file': 'arthaud.pdf'},
    'poutou': { 'name': "Philippe Poutou", 'file': 'poutou.pdf'},
    'melenchon' : { 'name': "Jean-Luc Mélenchon", 'file': 'melenchon.pdf'},
    'cheminade': { 'name': "Jacques Cheminade", 'file': 'cheminade.pdf'},
    'hamon' : { 'name': "Benoît Hamon", 'file': 'hamon.pdf'},
    'macron' : { 'name': "Emmanuel Macron", 'file': 'macron.pdf'},
    'lassalle' : { 'name': "Jean Lassalle", 'file': 'lassalle.pdf'},
    'fillon' : { 'name': "François Fillon", 'file': 'fillon.pdf'},
    'nda' : { 'name': "Nicolas Dupont-Aignan", 'file': 'nda.pdf'},
    'asselineau' : { 'name': "François Asselineau", 'file': 'asselineau.pdf'},
    'le-pen' : { 'name': "Marine Le Pen", 'file': 'le-pen.pdf'},
}
