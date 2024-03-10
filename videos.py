import requests

def search_youtube_videos(api_key, keywords):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": keywords,
        "type": "video",
        "key": api_key,
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Extract video information from the response
    video_links = []
    for item in data.get("items", []):
        video_id = item["id"]["videoId"]
        video_title = item["snippet"]["title"]
        video_links.append({"title": video_title, "link": f"https://www.youtube.com/watch?v={video_id}"})

    return video_links

# Example usage
api_key = "AIzaSyBEIpSazJA-yfulAQE0IO0RsXRmQP-rOV4"
keywords = "yoga pose tutorial"
videos = search_youtube_videos(api_key, keywords)

for video in videos:
    print(f"{video['title']}: {video['link']}")
