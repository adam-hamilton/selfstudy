'''doc'''

import requests



MYURL = 'http://sixty-north.com/c/t.txt'

def getUrl(url, *args, **kwargs):
    '''doc'''
    R = requests.get(MYURL, params=None)
    REPONSE = R.text
    return REPONSE

data = getUrl(MYURL)
print(data)