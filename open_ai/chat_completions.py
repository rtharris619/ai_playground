import os
from dotenv import load_dotenv
from openai import OpenAI
import time
from pathlib import Path
from enum import Enum

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_text():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming "
                                          "concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )

    print(completion.choices[0].message.content)


def generate_image():

    response = client.images.generate(
        model="dall-e-3",
        prompt="a golden labrador",
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    print(image_url)

    # Cats:
    # https://oaidalleapiprodscus.blob.core.windows.net/private/org-Ybu6ieCHE9HjcoIWRfId51HX/user-pFkgkIFFtFMJ1wmeBRKYjheq/img-wy9LDR1ojHVZOf7hqgCkEHTq.png?st=2024-03-06T13%3A40%3A28Z&se=2024-03-06T15%3A40%3A28Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-03-06T14%3A40%3A28Z&ske=2024-03-07T14%3A40%3A28Z&sks=b&skv=2021-08-06&sig=V2oWQvo2NV20j1rU0mgFrCh4w0DXEf2dYNk8EB4I2GA%3D
    # https://oaidalleapiprodscus.blob.core.windows.net/private/org-Ybu6ieCHE9HjcoIWRfId51HX/user-pFkgkIFFtFMJ1wmeBRKYjheq/img-14thWRseLmfASdRm1BwSZxQx.png?st=2024-03-06T13%3A39%3A17Z&se=2024-03-06T15%3A39%3A17Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-03-06T14%3A06%3A09Z&ske=2024-03-07T14%3A06%3A09Z&sks=b&skv=2021-08-06&sig=hA44rhb5oE2d8qez0F2hXgi%2BrR7p24vUlTwNYXg7eU0%3D

    # Dogs:
    # https://oaidalleapiprodscus.blob.core.windows.net/private/org-Ybu6ieCHE9HjcoIWRfId51HX/user-pFkgkIFFtFMJ1wmeBRKYjheq/img-MrJCQiMn7JIGN4KKYNO8JXlF.png?st=2024-03-06T13%3A47%3A12Z&se=2024-03-06T15%3A47%3A12Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-03-06T13%3A47%3A20Z&ske=2024-03-07T13%3A47%3A20Z&sks=b&skv=2021-08-06&sig=V68ISNh9ExL876%2BwLZ6pJc5hULdTU3JmplvypUUTbIk%3D


def use_assistant():
    assistant = client.beta.assistants.create(
        name="Math Tutor",
        instructions="You are a personal math tutor. Write and run code to answer math questions.",
        tools=[{"type": "code_interpreter"}],
        model="gpt-4-turbo-preview"
    )

    thread = client.beta.threads.create()

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
    )

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
        instructions="Please address the user as Ryan Harris. The user has a premium account."
    )

    attempts = 10
    current = 1
    busy = True

    while busy and attempts != current:
        check_run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )

        if check_run.status == 'completed':
            messages = client.beta.threads.messages.list(
                thread_id=thread.id
            )

            for data in messages.data:
                if data.role == 'assistant':
                    content = data.content[0]
                    print(content.text.value)

            busy = False

        if check_run.status == 'failed' or check_run.status == 'expired':
            print('error retrieving')
            busy = False

        if check_run.status == 'queued' or check_run.status == 'in_progress':
            print('queueing ' + str(current))
            time.sleep(2)

        current += 1


def use_vision():
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in the image?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/"
                                   "Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-"
                                   "wisconsin-madison-the-nature-boardwalk.jpg"
                        }
                    }
                ]
            }
        ],
        max_tokens=300
    )

    choice = response.choices[0]
    if choice:
        print(choice.message.content)

    # 1.
    # 'The image shows a wooden boardwalk stretching through a lush green grassy area.
    # The boardwalk is leading towards the horizon and is surrounded on both sides by tall grasses.
    # The sky above is partly cloudy with a mix of blue sky and white clouds, suggesting a nice day with good weather.
    # The scene appears serene, and the landscape is likely a natural reserve or a park where the boardwalk is meant
    # for visitors to enjoy the scenery without disturbing the natural vegetation.'

    # 2.
    # This image shows a scenic natural landscape featuring a wooden boardwalk or path extending through a grassy field.
    # The field is lush with vibrant green grass and a variety of wild plants. In the distance, you can see a line of
    # trees and shrubs marking the horizon. The sky is a soft blue, dotted with wispy white clouds, suggesting a calm
    # and fair weather day. The image conveys a sense of tranquility and the beauty of a natural, open space.


class Voice(Enum):
    Alloy = 'alloy'
    Echo = 'echo'
    Fable = 'fable'
    Onyx = 'onyx'
    Nova = 'nova'
    Shimmer = 'shimmer'


def text_to_speech():

    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice=Voice.Shimmer.value,
        input="Today is a wonderful day to build something people love!"
    )

    response.stream_to_file(speech_file_path)


def driver():
    text_to_speech()
