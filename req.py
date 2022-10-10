from urllib import request

url = 'http://127.0.0.1:80/'
count = 10000

for i in range(1, count+1):
    response = request.urlopen(url)
    print(f'code: {response.getcode()}')

