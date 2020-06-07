import json
import requests


list_of_champs = []

def get_Champ_Names():
    with open('champs.json') as f:
        data = json.load(f)

        for name in data['champions']:
            list_of_champs.append(str(name['name']))

        champ_dict = {
            'names':list_of_champs,
        }

        json_ = json.dumps(champ_dict)
        with open('champs_dict.json','w') as f:
            f.write(json_)

if __name__ == '__main__':
    get_Champ_Names()
