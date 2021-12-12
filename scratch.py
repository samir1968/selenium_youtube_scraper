import requests
from bs4 import BeautifulSoup

YOUTUBE_TRENDING_URL="https://www.youtube.com/feed/trending"


# Does not excute Javascript
response = requests.get(YOUTUBE_TRENDING_URL)

print("response status code", response.status_code)
#print("output", response.text[:1000])

#with open("Trending.html", "w") as f:
#  f.write(response.text)
#f.close()

doc = BeautifulSoup(response.text, 'html.parser')
print("Page Title", doc.title.text)

video_divs = doc.find_all('div', class_='style-scope ytd-video-renderer')
print(f"Found {len(video_divs)} videos")