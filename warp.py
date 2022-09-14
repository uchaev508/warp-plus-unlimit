import requests
s = requests.get('https://httpbin.org')
print(s.text)
