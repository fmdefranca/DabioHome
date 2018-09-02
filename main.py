import requests

response = requests.get('https://httpbin.org/user-agent')
print('Your IP is {}'.format(response.json()['user-agent']))
