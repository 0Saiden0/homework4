import requests
import threading
import os

urls = [
    'https://terraria.wiki.gg/images/4/4d/Terra_Blade.png',
    'https://terraria.wiki.gg/images/8/88/Eye_of_Cthulhu_%28Phase_1%29_%28old%29.png',
    'https://terraria.wiki.gg/images/7/7f/Guide.png',
    'https://terraria.wiki.gg/images/7/79/Queen_Slime.png',
    'https://terraria.wiki.gg/images/0/05/Life_Crystal.png'
]

def download(url):
        response = requests.get(url)
        filename = os.path.basename(url.encode('utf-8'))
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f'Download {url}!')
    
    

threads = []

for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()
    
    
for thread in threads:
    thread.join()