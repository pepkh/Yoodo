import httpx
import asyncio
import json

async def fetch(url, params):
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        return response.json()

async def search_youtube_videos(api_key, keywords, max_results=5):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": keywords,
        "type": "video",
        "maxResults": max_results,
        "key": api_key,
    }
    data = await fetch(url, params)
    
    # Debugging: Print the API response to inspect
    print(json.dumps(data, indent=4))

    # Extract video information from the response
    video_links = []
    if "items" in data:
        for item in data["items"]:
            video_id = item["id"]["videoId"]
            video_title = item["snippet"]["title"]
            video_links.append({"title": video_title, "link": f"https://www.youtube.com/watch?v={video_id}"})
    else:
        print("No items found in response.")

    return video_links

def get_embedded_link(video_link):
    return video_link.replace("/watch?v=", "/embed/")
