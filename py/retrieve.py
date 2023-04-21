from bs4 import BeautifulSoup
import html
import json
import re
import requests



API_KEY = "AIzaSyCx6qFDKefTEEC6uayva-xRuH7hNyaRPNU"
API_ENDPOINT = "https://www.googleapis.com/youtube/v3/search"

def get_channel_id(channel_url):
    resp = requests.get(channel_url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    # https://www.youtube.com/channel/channel_url
    og_url = soup.select_one('meta[property="og:url"]')['content']

    channel_id = og_url.strip('/').split('/')[-1]
    return channel_id

def main():

    channel_url = "https://www.youtube.com/@L0CKLEY"
    channel_id = get_channel_id(channel_url)

    params = {
        "part": "id,snippet",
        "channelId": channel_id,
        "maxResults": 50,
        "order": "date",
        "type": "video",
        "key": API_KEY,
    }

    # Make the API request to retrieve the list of videos from the channel
    response = requests.get(API_ENDPOINT, params=params).json()

    # Extract the video URLs and titles from the response
    videos = []
    for item in response["items"]:
        video_url = f'https://www.youtube.com/watch?v={item["id"]["videoId"]}'
        
        # get video title, then decode html entities
        video_title = html.unescape(item["snippet"]["title"])

        videos.append((video_url, video_title))

    # Print the list of videos
    for video in videos:
        print(video)
if __name__ == '__main__':
    main()