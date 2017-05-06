from nltk.twitter import Query, Streamer, Twitter, TweetViewer, TweetWriter, credsfromfile
from settings import *
import nltk
import sys
import re
import unicodedata
nb_tweets = 150
cons = ['refuse', 'stole', 'weak', 'monster', 'racist', 'leak,''bad', 'fascist', 'loose', 'lost', 'secret', 'trump', 'disagre', 'hate', 'crazy', 'conspirac']
pros = ['hope', 'good', 'great', 'president', 'faith', 'lead', 'better', 'win', 'vote for', 'agree', 'equality', 'love', 'visionnary', 'together']
candidates_tweets = [       
    { 'name': "emmanuel macron", 'pro' : 0 , 'cons' : 0},
    { 'name': "marine le pen", 'pro' : 0 , 'cons' : 0},
    { 'name': "francois fillon", 'pro' : 0 , 'cons' : 0},
    { 'name': "jean luc melanchon", 'pro' : 0 , 'cons' : 0},
    { 'name': "benoit hamon", 'pro' : 0 , 'cons' : 0},
    { 'name': "philippe poutou", 'pro' : 0 , 'cons' : 0},
    { 'name': "nicolas dupont aignan", 'pro' : 0 , 'cons' : 0},
    { 'name': "jean lasalle", 'pro' : 0 , 'cons' : 0},
    { 'name': "nathalie arthaud", 'pro' : 0 , 'cons' : 0},
    { 'name': "jacques cheminade", 'pro' : 0 , 'cons' : 0},
    { 'name': "francois asselineau", 'pro' : 0 , 'cons' : 0},
]


def analyze_tweets(candidate,tweets,subject):
    for tweet in tweets:
        tokens = nltk.word_tokenize(tweet['text'], 'english')
        for token in tokens:
            t = unicodedata.normalize('NFD', token).encode('ascii', 'ignore')
            for c in cons:                                
                reg = re.compile(r".*" + c + ".*")
                if re.search(reg, t.decode('utf-8')):
                    candidate['cons'] += 1
            for p in pros:                                
                reg = re.compile(r".*" + p + ".*")
                if re.search(reg, t.decode('utf-8')):             
                    candidate['pro'] += 1

    
def print_results(candidate,subject):
    print('\n'+candidate['name'])       
    print("\n"+subject+" :")
    print("Mots concernées : " + str(candidate['pro']+candidate['cons']))
    print("Avis pour : " + str(candidate['pro']))
    print("Avis contre : " + str(candidate['cons']))
    print("Sans avis : " + str(nb_tweets-(candidate['pro']+candidate['cons'])))
    print("Indice pour : " + str(candidate['pro']/nb_tweets))
    print("Indice contre : " + str(candidate['cons']/nb_tweets))
    if(candidate['pro']>candidate['cons']):
        print("Les gens sont pour ce candidat")
    elif(candidate['cons']>candidate['pro']):
        print("Les gens sont contre ce candidat")
    else:
        print("Les gens sont partagés")
    print('\n\n')

if __name__ == '__main__':
    print("Loadind tweets & analyzing ...")
    subject = 'people_tweets'
    for candidate in candidates_tweets:
        tw = Twitter()
        oauth = credsfromfile()
        client = Query(**oauth)
        tweets = client.search_tweets(keywords=candidate['name'], limit=nb_tweets)
        analyze_tweets(candidate,tweets,subject)      
    
        print_results(candidate,subject)
