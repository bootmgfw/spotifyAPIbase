# Import Spotify API
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import argparse
from os import system, name
from time import sleep
# Authenticate with the Spotify API
cid = ''
secret = ''
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)  

# Search for a song by the track name provided in the --track argument
def search_song(name): 
    result = sp.search(name, type='track')
    print('\nTop 10 results for search of:', name)
    for i, t in enumerate(result['tracks']['items'][:10]):
        print(i + 1, '-', t['name'], '-', t['artists'][0]['name'], '-', t['id'])
    song_choice = input('Enter a song number: ')
    song_id = result['tracks']['items'][int(song_choice) - 1]['id']
    return song_id


# Get info on the track selected inside of search_song()
def get_track_info(track_id):
    name = sp.track(track_id)['name']
    artist_id = sp.track(track_id)['album']['artists'][0]['id']
    genres_array = sp.artist(artist_id)['genres']
    genres_string = ' | '.join(genres_array)
    danceability = sp.audio_features(track_id)[0]['danceability']
    energy = sp.audio_features(track_id)[0]['energy']
    loudness = sp.audio_features(track_id)[0]['loudness']
    tempo = sp.audio_features(track_id)[0]['tempo']
    time_signature = sp.audio_features(track_id)[0]['time_signature']
    artist = sp.track(track_id)['artists'][0]['name']
    album = sp.track(track_id)['album']['name']
    length = sp.track(track_id)['duration_ms']
    minutes = int(length/1000/60)
    seconds = int((length/1000) - (minutes*60))
    # Pretty print the information stored in the variables above, including ms converted to minutes and seconds
    print(f'Track: {name}\nArtist: {artist}\nAlbum: {album}\nGenre: [{genres_string}]\nTime: {minutes}m:{seconds}s\nDanceability: {danceability}\nTime Signature: {time_signature}\nEnergy: {energy}\nTempo: {tempo}\nLoudness: {loudness}\n')
    main()
    



def main():
    name = input("Song Name: ")
    song_id = search_song(name)
    get_track_info(song_id)
    

main()


#REDUNDANT python3 module1.py --track Funny Monkey Friday

