import json
import requests
import bs4 as bs
import champs_dict as CP

list_of_champs = []
desc = []


def unpack_name():
    for name in CP.CHAMPION_DICT['names']:
        list_of_champs.append(name)

def parseDescription():
    for i in range(len(list_of_champs)):
        bio_url =  'https://universe.leagueoflegends.com/en_US/story/champion/{champName}/'.format(champName=list_of_champs[i].lower())
        r = requests.get(bio_url)
        soup = bs.BeautifulSoup(r.content,'lxml')

        for x in soup.head.find_all('meta', property='og:description'):
            desc.append(x['content'].encode('UTF-8'))

    dict = {
        'name': desc,
    }
    json_dict = json.dumps(dict)
    with open('champs_desc_dict.json','w') as f:
        f.write(json_dict)

if __name__ == '__main__':
    unpack_name()
    parseDescription()
