import base64, requests, os

API_ENDPOINT = 'https://discordapp.com/api/v6'
TOKEN = os.environ['w6_4mCE9La9oapNEnlAbvizV2et_vy1w']
CLIENT_ID = '804808860270460988'

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
