import cohere
COHERE_KEY = "rrtLFlHZgdlrIJLMb1svB8Khu57ft5aljM34Bizi"
co=cohere.Client(COHERE_KEY)

def generate_text(prompt, temp):
  response = co.chat(
    message=prompt,
    temperature=temp,
    stream=True)

  generated_text = []

  for event in response:
      if event.event_type == "text-generation":
        generated_text.append(event.text)
  cohere_recommendations_text = ''.join(generated_text)

  l_1 = cohere_recommendations_text.split(":", 1)
  l_2 = cohere_recommendations_text.split("2.")
  l_3 = cohere_recommendations_text.split("3.")
  tmp=l_2[1].split(":",1)
  temp_2=l_3[1].split(":",1)
  first_pose = l_1[0].split(".")[1]
  second_pose = l_2[1].split(":")[0]
  third_pose = l_3[1].split(":")[0]
#   description_1 = l_1[1].split("2")[0]
# # # # print(tmp)
#   description_2 = tmp[1].split("3")[0]
#   description_3 = temp_2[1]

  return [{'title':first_pose}, {'title':second_pose}, {'title':third_pose}]
  # return [{'title':first_pose,
  #         'benefit':description_1}, {'title':second_pose,
  #         'benefit':description_2}, {'title':third_pose,
  #         'benefit':description_3}]


  # poses = []
  # # Split by "1.", "2.", and "3." to find pose sections
  # pose_sections = cohere_recommendations_text.split('\n')[1:]  # Skip the first element if it's an intro or empty
  
  # for section in pose_sections:
  #   split_section = section.split(":", 1)  # Split only once
  #   if len(split_section) >= 2:
  #     pose_name = split_section[0].strip()
  #     pose_description = split_section[1].strip()
  #     poses.append({'title': pose_name, 'benefit': pose_description})
  #   else:
  #     print(f"Could not parse section: {section}")

  # return poses

# user_input_mood = ["sad", "annoyed"]
# user_input_health = "period pain"

# prompt = f"""I want to know 3 yoga poses if I have a health condition as {user_input_health} and my mood is {user_input_mood}. I want their benefit based on the mood and health condition. I also want the steps to perform the yoga pose. I always want it in an enumerated format like: 1. POSE_NAME: Benefit: Steps: STEPS"""

# print(cohere_recommendations_text)

# # retrieving the poses as strings 
# l_1 = cohere_recommendations_text.split(":", 1)
# l_2 = cohere_recommendations_text.split("2.")
# l_3 = cohere_recommendations_text.split("3.")
# tmp=(l_2[1]).split(":",1)
# temp_2=l_3[1].split(":",1)
# first_pose = l_1[0].split(".")[1]
# second_pose = l_2[1].split(":")[0]
# third_pose = l_3[1].split(":")[0]

# # description_1 = l_1[1].split("2")[0]
# # # print(tmp)
# # description_2 = tmp[1].split("3")[0]
# # description_3 = temp_2[1]
# # print(description_1)
# print(first_pose)
# print(second_pose)
# print(third_pose)
# # print(description_1)
# # print(description_2)