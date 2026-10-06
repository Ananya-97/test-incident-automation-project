import requests
r = requests.get('https://jsonplaceholder.typicode.com/posts/3', timeout = 10)
print(r.raise_for_status())
data = r.json()
print(data)
print("ID: ", data["id"])
print("Title: ", data["title"])
