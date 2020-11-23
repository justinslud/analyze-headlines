import requests

# result = requests.get("http://127.0.0.1:5000/",
# params = { 'headline': '' })
# print(result.json())

result = requests.post("http://127.0.0.1:5000/",
json = {'headline': 'Usain bolt wins the 100 meter dash in the London 2012 Olympics.'})
print(result.json())
