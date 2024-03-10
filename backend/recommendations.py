import cohere
import asyncio

COHERE_KEY = "rrtLFlHZgdlrIJLMb1svB8Khu57ft5aljM34Bizi"
co = cohere.Client(COHERE_KEY)

async def generate_text(prompt, temp=0):
    def sync_generate_text():
        response = co.chat(
            message=prompt,
            temperature=temp,
            stream=True
        )
        
        generated_text = []
        for event in response:
            if event.event_type == "text-generation":
                generated_text.append(event.text)
        return ''.join(generated_text)

    # Use asyncio.to_thread to run the synchronous function in a separate thread
    return await asyncio.to_thread(sync_generate_text)
