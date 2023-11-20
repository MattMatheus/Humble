"""Obviously we need the openai module"""
import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get('OPENAI_API_KEY')
messages = []
messages.append({ "role": "system", "content": "You are a quiz.  Present the user with a \
                  multiple-choice question to practice for a python interview, they have \
                  to respond by typing a, b, c, d or e.  \
                  Wait until the user responds before presenting a new question."})


while True:
    response = openai.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    print(response.choices[0].message.content)
    messages.append(response.choices[0].message)

    user_input = input("What is your answer?: ")
    if user_input == 'q' or user_input == 'quit':
        break
    messages.append({"role": "user", "content": user_input})
