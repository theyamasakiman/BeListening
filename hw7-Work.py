#Spotify API key: 81ea18661eda4b758e99424bb7c4439c
#Spotify API secret: 677c14c9912c47069011bd2f5d052923
#https://api.spotify.com/v1/albums/
#https://api.spotify.com/v1/artists/
#Parameters: v1/search?{album, artist, track, year, upc, tag:hipster, tag:new, isrc, and genre. }
#Limit:int
#redirect uri: http://localhost/
#response_type, client_id
from urllib import parse, request, error
import json
from urllib.request import urlopen

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

paramstr_token = parse.urlencode({'response_type': 'code','client_id':'81ea18661eda4b758e99424bb7c4439c','redirect_uri': 'http://localhost/'})
paramstr = parse.urlencode({'year': '2010', 'album': '24k Magic', 'artist': 'Bruno Mars', 'Bearer': '81ea18661eda4b758e99424bb7c4439c'})
baseurl = 'https://api.spotify.com/v1/search'
baseurl_auth = 'https://accounts.spotify.com/authorize'
spotify_auth = "?".join([baseurl_auth, paramstr_token])
print(spotify_auth)
spotify_token = urlopen(spotify_auth)
#spotify_data = json.loads(spotify_token.read())
print(pretty(spotify_auth))
#spotify_request = "?".join([baseurl,paramstr])

def get_song_data(year, album, artist):
    paramstr = parse.urlencode({'year': '2010', 'album': '24k Magic', 'artist': 'Bruno Mars', 'appid': '81ea18661eda4b758e99424bb7c4439c'})
    spotify_request = "?".join([baseurl, paramstr])
    spotify_request_api = urlopen(spotify_request)
    #print(sun_response_str)
    spotify_data = json.loads(spotify_request_api.read())
    return spotify_data
