import requests

def search_track(query):
    url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": "Bearer YOUR_SPOTIFY_TOKEN"}
    params = {"q": query, "type": "track", "limit": 5}
    response = requests.get(url, headers=headers, params=params)
    return response.json()
