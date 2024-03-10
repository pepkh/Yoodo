import requests

def search_youtube_videos(api_key, keywords, max_results=5):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": keywords,
        "type": "video",
        "maxResults": max_results,  # Set the maximum number of results
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

def choose_best_video(video_links, cohere_api_key):
    # You would need to implement logic to send the video titles to Cohere API for evaluation
    # and then choose the best one based on the API's response.
    # This is a simplified example; actual implementation would depend on the Cohere API.

    # Assuming Cohere API takes a list of texts and returns the best one
    titles = [video["title"] for video in video_links]
    best_title = send_titles_to_cohere(titles, cohere_api_key)

    # Find the corresponding video link for the best title
    best_video = next((video for video in video_links if video["title"] == best_title), None)

    return best_video

def send_titles_to_cohere(titles, cohere_api_key):
    # Implement logic to send titles to Cohere API and get the best one
    # This is a placeholder function; you need to replace it with the actual API integration
    return titles[0]  # Just returning the first title as a placeholder

def get_embedded_link(video_link):
    # Convert the regular YouTube link to an embedded link
    # Example: https://www.youtube.com/watch?v=VIDEO_ID -> https://www.youtube.com/embed/VIDEO_ID
    return video_link.replace("/watch?v=", "/embed/")

api_key = "AIzaSyBEIpSazJA-yfulAQE0IO0RsXRmQP-rOV4"
cohere_api_key = "YOUR_COHERE_API_KEY"
keywords = "yoga pose tutorial"
max_results = 5

videos = search_youtube_videos(api_key, keywords, max_results)

best_video = choose_best_video(videos, cohere_api_key)

if best_video:
    embedded_link = get_embedded_link(best_video['link'])
    print(f"The best video is: {best_video['title']} - {embedded_link}")
else:
    print("No videos found.")
