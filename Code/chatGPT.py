import openai

openai.api_key = "$$-$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"

def sendChatGPTMessage(text):
    messages = [
        {
            "role": "user",
            "content": text
        },
    ]
        
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    return chat.choices[0].message.content