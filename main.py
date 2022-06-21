from bs4 import BeautifulSoup
import requests as rq


LINK = "https://www.billboard.com/charts/hot-100/"

response = rq.get(url=LINK)
webpage = response.text


soup = BeautifulSoup(webpage, "html.parser")
artists = soup.find_all(name="span", class_="a-no-trucate")
titles = soup.find_all(name="h3", class_="a-font-primary-bold-s")

song_artists = [artist.getText().replace("\n", "").strip() for artist in artists]
song_titles = [title.getText().replace("\n", "").strip() for title in titles[2:]]


with open("top_100_songs.txt", "w") as file:
    for i in range(len(song_artists)):
        file.write(f"Position {i +1}: {song_titles[i]} by {song_artists[i]}")
        file.write("\n")
