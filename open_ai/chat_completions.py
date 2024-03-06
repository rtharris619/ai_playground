import os
from dotenv import load_dotenv
from openai import OpenAI

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


def driver():
    generate_text()
