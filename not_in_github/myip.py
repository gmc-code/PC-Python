import requests

url = 'http://myexternalip.com/raw'
r = requests.get(url)
ip = r.text