import openai
import os
from dotenv import find_dotenv, load_dotenv
import time
import logging
from datetime import datetime
import requests
import json
import streamlit as st

load_dotenv()



client = openai.OpenAI()
# model = "gpt-3.5-turbo-16k"

#================================================================================================

response = client.images.generate(
  model="dall-e-3",
  prompt="a wooden boardwalk leading through a lush green meadow or wetland area. The grass and vegetation on either side of the boardwalk are dense and tall, suggesting a natural, possibly preserved or untouched environment. Above, there is a beautiful blue sky with scattered clouds, indicating fair weather. The setting appears peaceful and is likely a place for walking, nature observation, or conservation. There are no people visible in the image",
  # prompt="大漠孤烟直，长河落日圆",
  # prompt="鲁智深倒拔垂杨柳",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
st.image(image_url, caption="Generated Image") 
st.write(image_url)

#================================================================================================
# response = client.images.create_variation(
#   image=open("example.png", "rb"),
#   n=2,
#   size="1024x1024"
# )

# image_url = response.data[0].url
# st.image(image_url, caption="Generated Image")
# st.write(image_url)
#================================================================================================
# image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
# response = client.chat.completions.create(
#   model="gpt-4-vision-preview",
#   messages=[
#     {
#       "role": "user",
#       "content": [
#         {"type": "text", "text": "What’s in this image?"},
#         {
#           "type": "image_url",
#           "image_url": {
#             "url": image_url,
#           },
#         },
#       ],
#     }
#   ],
#   max_tokens=300,
# )

# print(response.choices[0])
# st.image(image_url, caption="feeding Image to model")
# st.write(response.choices[0].message.content)
#================================================================================================
