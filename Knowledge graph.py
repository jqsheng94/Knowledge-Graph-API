import re
import urllib.request
import simplejson as json
from bs4 import BeautifulSoup
from lxml import html
import requests
from os.path import basename
from urllib.request import urlopen




important_terms = ['Minecraft', 'أم كلثوم']
for i in important_terms:
    i = urllib.parse.quote(i)
    link = json.load(
        urlopen(
            "https://kgsearch.googleapis.com/v1/entities:search?query=" + i + "&key=AIzaSyCilPTC0yjLoKGLkCUp0C_ZJmJoAI3ygH4&limit=1&indent=True"))
    Output = link['itemListElement']
    for element in Output:
        if '@type' in element['result']:
            word_type = element['result']['@type']
        if "description" in element['result']:
            description = element['result']['description']
        if "detailedDescription" in element['result']:
            articleBody = element['result']['detailedDescription']['articleBody']
        else:
            articleBody =''
        if 'name' in element['result']:
            name = element['result']['name']
            print('===Name===')
            print(name)
            print('===desecription===')
            print(description)
            print('===Article===')
            print(articleBody)


