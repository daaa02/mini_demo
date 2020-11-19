import asyncio

from mini import mini_sdk as MiniSdk
from mini.apis.api_sound import StartPlayTTS
from mini.mini_sdk import WiFiDevice


async def _play_tts():
    block: StartPlayTTS = StartPlayTTS(text="hello! i'm alphamini, test, test, test")
    # return (), response is `ControlTTSResponse`
    (resultType, response) = await block.execute()
    print(f'{response}')


async def _run():
    device: WiFiDevice = await MiniSdk.get_device_by_name("0090", 10)
    if device:
        await MiniSdk.connect(device)
        await MiniSdk.enter_program()
        await _play_tts()
        await MiniSdk.quit_program()
        await MiniSdk.release()


def main():
    asyncio.run(_run())


if __name__ == '__main__':
    main()
