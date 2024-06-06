import requests
import os

urls = [
    'https://terraria.wiki.gg/images/4/4d/Terra_Blade.png',
    'https://terraria.wiki.gg/images/8/88/Eye_of_Cthulhu_%28Phase_1%29_%28old%29.png'
]

for url in urls:
    response = requests.get(url)
    filename = os.path.basename(url.encode('utf-8'))
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f'Download {url}!')