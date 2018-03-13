import requests
from lxml import etree
from io import StringIO

bird_max = 491
birds_url = 'https://avian.lib.iastate.edu/birds/{}/view'
gbif_url = 'http://api.gbif.org/v1/species/{}'
output_file = 'C:/path/to/my.csv'

parser = etree.HTMLParser()
birds = {}

for n in range(1, bird_max + 1):
    r = requests.get(birds_url.format(n))
    tree = etree.parse(StringIO(r.text), parser)
    id_ = tree.xpath('//th[text()="Species ID #"]/following-sibling::td')[0].text
    name = tree.xpath('//th[text()="Common Name"]/following-sibling::td')[0].text
    birds[id_] = {'name': name}

for k, v in birds.items():
    r = requests.get(gbif_url.format(k))
    info = r.json()
    v['rank'] = info['rank']
    v['status'] = info['taxonomicStatus']
    
with open(output_file, 'w') as fh:
    for k, v in birds.items():
        fh.write(f'{k},"{v["name"]}",{v["rank"]},{v["status"]}\n')

    

