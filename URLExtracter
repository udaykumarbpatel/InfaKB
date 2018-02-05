# https://cloudplatform.coveo.com/rest/search/v2/

import json

f = open('urls.txt', 'a+')

with open('input.json', 'r') as fp:
    obj = json.load(fp)

for x in obj['results']:
    f.write(x['raw']['clickableuri'])
    f.write('\n')

f.close()
