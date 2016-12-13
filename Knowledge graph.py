# This script is to search name, word type and description of any term.
import urllib.request
import simplejson as json
from urllib.request import urlopen



Key = 'PUT YOUR KEY HERE'
important_terms = ['Minecraft', 'أم كلثوم']
for i in important_terms:
    i = urllib.parse.quote(i)
    link = json.load(
        urlopen("https://kgsearch.googleapis.com/v1/entities:search?query=" + i + "&key=" + Key + "&limit=1&indent=True"))
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
            print('===Name==================')
            print(name)
            print('===desecription==========')
            print(description)
            print('===Article===============')
            print(articleBody)




