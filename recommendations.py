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

user_input_mood = "happy"
user_input_health = "pain in knees"
user_input_duration = "5"

prompt = f"""Recommend 3 to 4 yoga poses for a person with health condition as {user_input_health} and  with mood {user_input_mood}. Insert an underscore symbol between the description and the steps."""

generate_text(prompt, temp=0.5)