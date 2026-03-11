import urllib.request
import re

id = "tt6946962"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

try:
    url = f'https://www.imdb.com/title/{id}/'
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req).read().decode('utf-8')
    og_images = re.findall(r'<meta[^>]+property="og:image"[^>]*>', html)
    print("OG Images:", og_images)
    
    images = re.findall(r'https://m\.media-amazon\.com/images/M/[^"\'>\s]+', html)
    print("\nAmazon Images:", images[:5])
    
    with open('imdb_debug.html', 'w', encoding='utf-8') as f:
        f.write(html)
except Exception as e:
    print(f'{id}: Error - {e}')
