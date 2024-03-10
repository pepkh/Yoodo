import cohere
COHERE_KEY = "rrtLFlHZgdlrIJLMb1svB8Khu57ft5aljM34Bizi"
co=cohere.Client(COHERE_KEY)

def generate_text(prompt, temp=0):
  response = co.chat(
    message=prompt,
    temperature=temp,
    stream=True)

  for event in response:
      if event.event_type == "text-generation":
          print(event.text, end='')

user_input_mood = ["happy", "excited"]
user_input_health = "pain in knees"

prompt = f"""I want to know 3 yoga poses if I have a health condition as {user_input_health} and my mood is {user_input_mood}. I want their use based on the mood and health condition. I also want the steps to perform the yoga pose. I want it in an enumerated format like: 1. POSE_NAME: Use: Steps: STEPS"""

cohere_recommendations_text = generate_text(prompt, temp=0.5)


l_1 = cohere_recommendations_text.split("1.")
l_2 = cohere_recommendations_text.split("2.")
l_3 = cohere_recommendations_text.split("3.")
first_pose = l_1[0]
second_pose = l_2[0]
third_pose = l_3[0]


