import random

import requests

API_KEY = ""
playlistId = "PLE61688C0C6264341"
playlistItem_object = requests.get(f'https://content-youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&key={API_KEY}&maxResults=10&playlistId={playlistId}')
print(playlistItem_object)
playlistItemJson = playlistItem_object.json()
for item in (playlistItemJson['items']):
    print(item['contentDetails']['videoId'])
