'''doc'''

import requests



MYURL = 'http://sixty-north.com/c/t.txt'

def getUrl(url, *args, **kwargs):
    '''doc'''
    R = requests.get(MYURL, params=None)
    RESP = R.text.split()
    DATA = [line.split() for line in RESP]
    return DATA


data = getUrl(MYURL)
print(' \n'.join([str(i.split()), for i in data]))
#print(data)

#from urllib.request import urlopen
def words(url):
    with requests.get(url, params=None) as story:
    #with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    for word in story_words:
        print (word)

#words(MYURL)