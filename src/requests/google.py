import requests

ggl = requests.get('www.google.com')

print(ggl.status_code)
pri