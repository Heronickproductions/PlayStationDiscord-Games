import base64, requests, os

API_ENDPOINT = 'https://discordapp.com/api/v6'
TOKEN = os.environ['K_Py3y8lGD4Di3fgFl830-kFE4HAuEkM']
CLIENT_ID = '765955183225208872'

def get_assets():
    r = requests.get('%s/oauth2/applications/%s/assets' % (API_ENDPOINT, CLIENT_ID), headers={'Authorization': '%s' % TOKEN})
    r.raise_for_status()
    return r.json()

def add_asset(name, image_data):
    data = {
        'name': name,
        'image': image_data,
        'type': 1
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': '%s' % TOKEN
    }
    r = requests.post('%s/oauth2/applications/%s/assets' % (API_ENDPOINT, CLIENT_ID), headers=headers, json=data)
    r.raise_for_status()
    return r.json()

def delete_asset(id):
    r = requests.delete('%s/oauth2/applications/%s/assets/%s' % (API_ENDPOINT, CLIENT_ID, id), headers={'Authorization': '%s' % TOKEN})
    r.raise_for_status()
