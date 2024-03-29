import requests
import recommendations
import cohere
api_key = "AIzaSyCASxWtiCMSsTb1Z63268R9341midscYb4"
cohere_api_key = "rrtLFlHZgdlrIJLMb1svB8Khu57ft5aljM34Bizi"

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

def get_embedded_link(video_link):
    return video_link.replace("/watch?v=", "/embed/")

def search_youtube_videos(api_key, keywords, max_results=1):
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
    print("video dataaaaaaa")
    video_links = []
    for item in data.get("items", []):
        video_id = item["id"]["videoId"]
        video_title = item["snippet"]["title"]
        video_links.append({"title": video_title, "link": f"https://www.youtube.com/watch?v={video_id}"})

    return video_links

# def choose_best_video(keyword,video_links):
#     #Assuming Cohere API takes a list of texts and returns the best one
#     titles = [video["title"] for video in video_links]
#     best_title = send_titles_to_cohere(keyword,titles)

#     #Find the corresponding video link for the best title
#     best_video = next((video for video in video_links if video["title"] == best_title), None)
#     return best_video

# def send_titles_to_cohere(keyword,titles):
#     prompt = f"Choose one video at random from the list of {titles} and return it as a list of single title"
#     best_title = generate_text(prompt, temp=0.5)
#     print(best_title)
#     return best_title

def get_embedded_link(video_link):
    return video_link.replace("/watch?v=", "/embed/")

# keyword1 = recommendations.first_pose
# keyword2 = recommendations.second_pose
# keyword3 = recommendations.third_pose
# print(keyword1)
# print(keyword2)
# print(keyword3)
# max_results = 1

# Search for 5 videos for each keyword
# video = search_youtube_videos(api_key, keyword, max_results)
# videos2 = search_youtube_videos(api_key, keyword2, max_results)
# videos3 = search_youtube_videos(api_key, keyword3, max_results)

# url = get_embedded_link(videos1[0]["link"])
# url2 = get_embedded_link(videos2[0]["link"])
# url3 = get_embedded_link(videos3[0]["link"])

# print(url1)
# print(url2)
# print(url3)

# Search and choose the best video for each keyword
# best_video1 = choose_best_video(keyword1,videos1)
# best_video2 = choose_best_video(keyword2,videos2)
# best_video3 = choose_best_video(keyword3,videos3)

# # Display the results
# for i, best_video in enumerate([best_video1, best_video2, best_video3], start=1):
#     if best_video:
#         embedded_link = get_embedded_link(best_video['link'])
#         print(f"The best video for Pose {i} is: {best_video['title']} - {embedded_link}")
#     else:
#         print(f"No videos found for Pose {i}.")