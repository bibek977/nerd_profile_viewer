import requests
import json

url = "http://127.0.0.1:8000/api/"

r_get = requests.get(url=url)

get_data = r_get.json()
print(get_data)

post_data = {
   "actor": "Bibek Bhattarai", "actress": "Zoe Saldana", "title": "Avatar", "director": "James Cameron", "writer": "James Cameron", "country": "USA", "year": 2009, "runtime": 162, "imdb": 7.9, "summary": "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home."
}

json_data = json.dumps(post_data)
r_post = requests.post(url=url, data=json_data)

print(r_post.json())