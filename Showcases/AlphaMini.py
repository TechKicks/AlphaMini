import mini.mini_sdk as MiniSdk
from mini.dns.dns_browser import WiFiDevice
import logging
from mini.apis.api_sound import PlayAudio
import openai
from mini.apis.api_sound import StartPlayTTS
import asyncio
from deep_translator import GoogleTranslator

async def ConnectToAlphaMini():
    MiniSdk.set_log_level(logging.INFO)
    MiniSdk.set_robot_type(MiniSdk.RobotType.EDU)

    result: WiFiDevice = await MiniSdk.get_device_by_name("Edu_030008KFK18122900534", 10)
    print(f"test_get_device_by_name result:{result}")

    if result:
        await MiniSdk.connect(result)
        await MiniSdk.enter_program()

async def translateAndSay(text, targetTranslate, targetTTS):
    # Translate reply
    text = GoogleTranslator(source='auto', target="nl").translate(text) 

    # Generate TTS Url Query
    api_url = "http://api.voicerss.org/?key="
    KEY = "cc4ba25d57e94db3884a609a7375f7c9"
    api_end = f"&hl=nl-nl&src="

    # Playing Audio
    print("Saying: " + text)
    action = PlayAudio(url=api_url + KEY + api_end + text)
    await action.execute()

async def listenToFirstAnswer(observer, onAnswer):
    action = StartPlayTTS(text="I'm Listening")
    await action.execute()

    observer.set_handler(onAnswer)
    observer.start()

