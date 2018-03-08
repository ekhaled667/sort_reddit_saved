import requests
from urllib import parse
from uuid import uuid4
from enum import Enum

oauth_url = 'https://oauth.reddit.com'

class reddit:
    def __init__(self, client_id, client_secret, redirect_uri, scope, user_agent):
        self.client_id = client_id
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.client_secret = client_secret
        self.user_agent = user_agent
        self.token = ''
        self.state = str(uuid4())
    
    def auth_url(self):
        parameters = {'client_id' : self.client_id,
                    'response_type' : 'code',
                    'state': self.state,
                    'redirect_uri' : self.redirect_uri,
                    'duration' : 'temporary',
                    'scope' : self.scope}
        return 'https://www.reddit.com/api/v1/authorize?' + parse.urlencode(parameters)

    def set_access_token(self, state, code):
        if state == self.state:
            req = requests.post('https://ssl.reddit.com/api/v1/access_token',
                        data={'grant_type' : 'authorization_code', 'code' : code, 'redirect_uri' : self.redirect_uri},
                        auth=requests.auth.HTTPBasicAuth(self.client_id, self.client_secret),
                        headers={'User-Agent' : self.user_agent})
            self.token = req.json()['access_token']
            self.header = {'Authorization' : 'bearer ' + self.token, 'User-Agent' : self.user_agent}
            self.name = self.get_user_name()

    def get_user_name(self):
        return requests.get(oauth_url + '/api/v1/me', headers=self.header).json()['name']

    def save_post(self, id):
        requests.post( oauth_url + '/api/save',
                        data={'id' : id},
                        headers=self.header)

    def unsave_post(self, id):
        requests.post(oauth_url + '/api/unsave',
                        data={'id' : id},
                        headers=self.header)

    def get_saved_posts(self, limit=25):
        assert(limit >= 0 and limit <=100)
        return requests.get(oauth_url + '/user/' + self.get_user_name() + '/saved' + '?raw_json=1&limit=' + str(limit),
        headers=self.header).json()['data']['children']

class sort_option(Enum):
    newest = 0
    oldest = 1
    ascending = 2
    subreddit_ascending = 3
    score = 4
    number_of_comments = 5