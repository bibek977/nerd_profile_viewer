import requests
import json

url = "http://127.0.0.1:8000/api/"

r_get = requests.get(url=url)

get_data = r_get.json()
print(get_data)

post_data = {
    'name' : 'bipin',
    'phone' : '98000000',
    'location' : 'hattiban',
    'program' : 'Django'
}

json_data = json.dumps(post_data)
r_post = requests.post(url=url, data=json_data)

print(r_post.json())