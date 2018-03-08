import webbrowser
from reddit_client import reddit, sort_option
from pathlib import Path

sort_citeria = sort_option.newest

r = reddit(client_id = '',
            client_secret = '',
            redirect_uri = 'http://localhost:65010/reddit_callback',
            scope = 'identity, history, save',
            user_agent = 'sort_reddit_saved 1.0 by ekhaled667')

webbrowser.open(r.auth_url())
x = input('Enter the callback URL: ')
r.set_access_token(state=x[x.find('state')+6:x.find('&')], code=x[x.find('code')+5:len(x)])
posts = []

with open(str(Path.home()) + '/Downloads/saved_posts', 'w') as file:
    while 1:
        temp = r.get_saved_posts(limit=100)
        if len(temp) == 0:
            break
        for item in temp:
            file.write(item['data']['name'] + '\n')
            r.unsave_post(id=item['data']['name'])
        posts.extend(temp)

if sort_citeria == sort_option.newest:
    posts.sort(key=lambda x:x['data']['created_utc'])
elif sort_citeria == sort_option.oldest:
    posts.sort(key=lambda x:x['data']['created_utc'], reverse=True)
elif sort_citeria == sort_option.ascending:
    posts.sort(key=lambda x:x['data']['title'])
elif sort_citeria == sort_option.subreddit_ascending:
    posts.sort(key=lambda x:x['data']['subreddit'])
elif sort_citeria == sort_option.score:
    posts.sort(key=lambda x:x['data']['score'])
elif sort_citeria == sort_option.number_of_comments:
    posts.sort(key=lambda x:x['data']['num_comments'])
    
for item in posts:
    r.save_post(id=item['data']['name'])