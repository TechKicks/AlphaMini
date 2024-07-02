import mini.mini_sdk as MiniSdk
from mini.dns.dns_browser import WiFiDevice
import logging
import asyncio
import os

SERIAL_NUMBER = "Edu_030008KFK18122900534"

async def connect():
    os.system('cls')
    MiniSdk.set_log_level(logging.CRITICAL)
    MiniSdk.set_robot_type(MiniSdk.RobotType.EDU)

    print("AlphaMini aan het zoeken...")
    result: WiFiDevice = await MiniSdk.get_device_by_name(SERIAL_NUMBER, 10)

    if result:
        os.system('cls')
        print("AlphaMini gevonden!")

        await MiniSdk.connect(result)
        await MiniSdk.enter_program()

        os.system('cls')
        print("Verbonden met AlphaMini!")
    else:
        os.system('cls')
        raise Exception("Kan niet verbinden met AlphaMini!")

if __name__ == "__main__":
    asyncio.run(connect())