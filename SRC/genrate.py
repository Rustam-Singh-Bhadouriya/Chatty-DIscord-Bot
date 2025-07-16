from tokin import API
# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def generate(msg):
    client = genai.Client(
        api_key=API,
    )

    model = "gemini-2.5-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"You are a discord bot chatty try to chat like humans as nother user chatting message = {msg} if message in hindi then response in hindi like (kaise ho!) but dont type hindi characters kaise ho aise bolna with emoji ans dont use hey there keyword and if english then response in english in low words around less then 15 words be humenize and fast response also"),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ),
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        # print(chunk.text, end="")
        return chunk.text

if __name__ == "__main__":
    generate()
