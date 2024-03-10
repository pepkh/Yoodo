# import requests
# import recommendations

# def search_youtube_videos(api_key, keywords, max_results=5):
#     url = "https://www.googleapis.com/youtube/v3/search"
#     params = {
#         "part": "snippet",
#         "q": keywords,
#         "type": "video",
#         "maxResults": max_results,  # Set the maximum number of results
#         "key": api_key,
#     }

#     response = requests.get(url, params=params)
#     data = response.json()

#     # Extract video information from the response
#     video_links = []
#     for item in data.get("items", []):
#         video_id = item["id"]["videoId"]
#         video_title = item["snippet"]["title"]
#         video_links.append({"title": video_title, "link": f"https://www.youtube.com/watch?v={video_id}"})

#     return video_links

# def choose_best_video(video_links, cohere_api_key):
#     # You would need to implement logic to send the video titles to Cohere API for evaluation
#     # and then choose the best one based on the API's response.
#     # This is a simplified example; actual implementation would depend on the Cohere API.

#     # Assuming Cohere API takes a list of texts and returns the best one
#     titles = [video["title"] for video in video_links]
#     best_title = send_titles_to_cohere(titles, cohere_api_key)

#     # Find the corresponding video link for the best title
#     best_video = next((video for video in video_links if video["title"] == best_title), None)

#     return best_video

# def send_titles_to_cohere(titles, cohere_api_key):
#     prompt = f"Evaluate the titles and find the best one: {titles}"
#     best_title = recommendations.generate_text(prompt, temp=0.5)
#     return best_title

# def get_embedded_link(video_link):
#     # Convert the regular YouTube link to an embedded link
#     # Example: https://www.youtube.com/watch?v=VIDEO_ID -> https://www.youtube.com/embed/VIDEO_ID
#     return video_link.replace("/watch?v=", "/embed/")

# api_key = "AIzaSyBEIpSazJA-yfulAQE0IO0RsXRmQP-rOV4"
# cohere_api_key = "rrtLFlHZgdlrIJLMb1svB8Khu57ft5aljM34Bizi"
# keyword1 = recommendations.first_pose
# keyword2 = recommendations.second_pose
# keyword3 = recommendations.third_pose
# max_results = 5

# video1 = search_youtube_videos(api_key, keyword1, max_results)
# video2 = search_youtube_videos(api_key, keyword2, max_results)
# video3 = search_youtube_videos(api_key, keyword3, max_results)

# best_video1 = choose_best_video(video1, cohere_api_key)
# best_video2 = choose_best_video(video2, cohere_api_key)
# best_video3 = choose_best_video(video3, cohere_api_key)

# if best_video1:
#     embedded_link1 = get_embedded_link(best_video1['link'])
#     print(f"The best video is: {best_video1['title']} - {embedded_link1}")
# else:
#     print("No videos found.")

# if best_video2:
#     embedded_link2 = get_embedded_link(best_video2['link'])
#     print(f"The best video is: {best_video2['title']} - {embedded_link2}")
# else:
#     print("No videos found.")


# if best_video3:
#     embedded_link3 = get_embedded_link(best_video3['link'])
#     print(f"The best video is: {best_video3['title']} - {embedded_link3}")
# else:
#     print("No videos found.")

import requests
import recommendations
import cohere

COHERE_KEY = "rrtLFlHZgdlrIJLMb1svB8Khu57ft5aljM34Bizi"
co = cohere.Client(COHERE_KEY)

def generate_text(prompt, temp=0):
    response = co.chat(
        message=prompt,
        temperature=temp,
        stream=True)

    generated_text = []

    for event in response:
        if event.event_type == "text-generation":
            generated_text.append(event.text)
    return ''.join(generated_text)

def send_titles_to_cohere(titles, cohere_api_key):
    prompt = f"I want a youtube video whose title best matches the following: {titles}"
    best_title = generate_text(prompt, temp=0.5)
    return best_title

def get_embedded_link(video_link):
    return video_link.replace("/watch?v=", "/embed/")

def search_youtube_videos(api_key, keywords, max_results=5):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": keywords,
        "type": "video",
        "maxResults": max_results,
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
    # Assuming Cohere API takes a list of texts and returns the best one
    titles = [video["title"] for video in video_links]
    best_title = send_titles_to_cohere(titles, cohere_api_key)

    # Find the corresponding video link for the best title
    best_video = next((video for video in video_links if video["title"] == best_title), None)

    return best_video

api_key = "AIzaSyBEIpSazJA-yfulAQE0IO0RsXRmQP-rOV4"
cohere_api_key = "rrtLFlHZgdlrIJLMb1svB8Khu57ft5aljM34Bizi"
keyword1 = recommendations.first_pose
keyword2 = recommendations.second_pose
keyword3 = recommendations.third_pose
max_results = 5

videos1 = search_youtube_videos(api_key, keyword1, max_results)
videos2 = search_youtube_videos(api_key, keyword2, max_results)
videos3 = search_youtube_videos(api_key, keyword3, max_results)

print(len(videos1))
print(len(videos2))
print(len(videos3))

# Search and choose the best video for each keyword
best_video1 = choose_best_video(search_youtube_videos(api_key, keyword1, max_results), cohere_api_key)
best_video2 = choose_best_video(search_youtube_videos(api_key, keyword2, max_results), cohere_api_key)
best_video3 = choose_best_video(search_youtube_videos(api_key, keyword3, max_results), cohere_api_key)

# Display the results
for i, best_video in enumerate([best_video1, best_video2, best_video3], start=1):
    if best_video:
        embedded_link = get_embedded_link(best_video['link'])
        print(f"The best video for Pose {i} is: {best_video['title']} - {embedded_link}")
    else:
        print(f"No videos found for Pose {i}.")


print(best_video1)
print(best_video2)
print(best_video3)
