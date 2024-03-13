from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import re
import recommendations  # Import your recommendations module
from videos import search_youtube_videos, get_embedded_link

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/generate_text', methods=['POST'])
def generate_text_route():
    # Get mood and health condition arrays from query parameters
    data = request.get_json()
    user_input_mood = ", ".join(data.get('user_input_mood', []))
    user_input_health = ", ".join(data.get('user_input_health', []))
    # Format the mood list into a single string if necessary
    
    # Construct the prompt based on the inputs
    prompt = f"""I want to know 3 yoga poses if I have a health condition as {user_input_health} and my mood is {user_input_mood}. I want their benefit based on the mood and health condition. I also want the steps to perform the yoga pose. I always want it in an enumerated format like: 1. POSE_NAME: Benefit: Steps: STEPS"""
    poses = recommendations.generate_text(prompt, temp=0.5)
    results = []
    api_key = "AIzaSyCASxWtiCMSsTb1Z63268R9341midscYb4"
    print(poses)
    # Call the generate_text function from your recommendations module
    for pose in poses:
        print(pose)
        print(pose['title'])
        videos =  search_youtube_videos(api_key, pose['title'], max_results=1,)
        if videos:
            print(videos[0]['link'])
            video_link =  get_embedded_link(videos[0]['link'])
            pose['video_link'] = video_link  # Add video link to pose information
        else:
            pose['video_link'] = "No video found"
        results.append(pose)
    return jsonify(results)
    # return jsonify([
    #     {
    #         'title': first_pose,
    #         'description': description_1,
    #     },
    #     {
    #         'title': second_pose,
    #         'description': description_2,
    #     }, 
    #     {
    #         'title': third_pose,
    #         'description': description_3,
    #     }
    # ])
# def parse_cohere_text_to_poses(text):
#     poses = []
#     # Split the text by "1.", "2.", and "3." to get individual pose descriptions
#     split_text = re.split(r'\n\d+\.', text)
#     for pose_text in split_text[1:]:  # Skip the first element, as it's before the first "1."
#         title_search = re.search(r'^(.*?):', pose_text)
#         title = title_search.group(1).strip() if title_search else "Unknown Pose"
        
#         description_search = re.search(r'Use:(.*?)Steps:', pose_text, re.DOTALL)
#         description = description_search.group(1).strip() if description_search else "No description provided"
        
#         poses.append({'title': title, 'description': description})
#     return poses

# def parse_cohere_text_to_poses(text):
#     l_1 = text.split(":", 1)
#     l_2 = text.split("2.")
#     l_3 = text.split("3.")
#     tmp=(l_2[1]).split(":",1)
#     temp_2=l_3[1].split(":",1)
#     first_pose = l_1[0].split(".")[1]
#     second_pose = l_2[1].split(":")[0]
#     third_pose = l_3[1].split(":")[0]

#     description_1 = l_1[1].split("2")[0]
# # print(tmp)
#     description_2 = tmp[1].split("3")[0]
#     description_3 = temp_2[1]# Placeholder implementation
#     return [{'title': first_pose,
#              'description': description_1}, 
#              {'title': second_pose,
#               'description': description_2},
#              {'title': third_pose,
#               'description': description_3}]

if __name__ == '__main__':
    app.run(debug=True)
