import urllib.request
import re

ids = [
    "tt33244668", # Anaconda
    "tt33479805", # Killer Whale
    "tt32247012", # A Series of Unfortunate Dates
    "tt6946962",  # Wolfe
    "tt39742493", # Far End of the Sea
    "tt31691565"  # Good Cop / Bad Cop
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

for id in ids:
    try:
        url = f'https://www.imdb.com/title/{id}/'
        req = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(req).read().decode('utf-8')
        match = re.search(r'meta property="og:image"\s+content="([^"]+)"', html)
        if match:
            print(f'{id}: {match.group(1)}')
        else:
            print(f'{id}: Not found')
    except Exception as e:
        print(f'{id}: Error - {e}')
