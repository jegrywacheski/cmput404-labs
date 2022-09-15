import requests

r = requests.get('https://raw.githubusercontent.com/jegrywacheski/cmput404-labs/main/request_version.py')

print(r.text) 
