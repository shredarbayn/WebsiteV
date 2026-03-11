import urllib.request
import json
import ssl
import sys

# Disable SSL check which may block some API requests locally
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

ids = {"tt33244668": "Anaconda", "tt33479805": "Killer Whale", "tt32247012": "A Series of Unfortunate Dates", 
       "tt6946962": "Wolfe", "tt39742493": "Far End of the Sea", "tt31691565": "Good Cop / Bad Cop"}

for id, name in ids.items():
    try:
        url = f'https://imdb-api.projects.thetuhin.com/title/{id}'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, context=ctx).read()
        data = json.loads(response)
        
        image = data.get('image', 'Not found')
        print(f"{name} ({id}): {image}")
    except Exception as e:
        print(f"{name} ({id}): Error - {e}")
