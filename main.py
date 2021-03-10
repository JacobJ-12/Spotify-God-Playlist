import requests
import json

def search_item(search, search_type, token):
  search_artist = f"https://api.spotify.com/v1/search?q={search}&&type={search_type}"
  response = requests.get (
    search_artist,
    headers = {
      "Authorization" : "Bearer " + token
    }
  )
  return response

def popularity_adder(token):
  artist = input("Enter an artist: ")
  popularity_min = int(input("What is the minimum popularity for the songs(1-100): "))
  search_response = search_item(artist, "artist",token)
  artist_id = search_response.json()["artists"]["items"][0]["id"]

  toptracks = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=US"
  toptracks_response = requests.get (
    toptracks,
    headers = {
      "Authorization": "Bearer " + token
    }
  )
  #tracks 0 album name
  tracks_list = []
  for x in range(0,10):
    track_popularity = toptracks_response.json()["tracks"][x]["popularity"]
    if track_popularity>popularity_min:
      tracks_list.append(toptracks_response.json()["tracks"][x]["id"])
  playlist_id = "7Hsj6192pO36j1AZYgJphB"
  for x in tracks_list:
    add_track = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?uris=spotify%3Atrack%3A{x}"
    requests.post (
      add_track,
      headers = {
        "Authorization": "Bearer " + token
      }
    )

token = "BQDndSekSazGfrLFF4OS7W950DdAjoi8ipoZVB7mGP8PwEUXRE1k73XwwbwHBXlt6EuMrAWrqkpSYht75Hldla8wiwfaubd3Kj7plyK-Rd3uPRYhBvYJ-c_Xjito-w4TKlK9m3IdKmKd62wvECfkAGc4f4o4RP8TZ_EtQopxqqh_bBuwFFtWa6tUW8uCeflT9BgTUckYWUnPn5hRFk2HwqJVKvZ0okz5"
artists_num = int(input("How many artists are you going to input: "))
for x in range(0,artists_num):
  popularity_adder(token)

