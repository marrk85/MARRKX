import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from YukkiMusic import LOGGER, app, userbot
from YukkiMusic.core.call import Yukki
from YukkiMusic.plugins import ALL_MODULES
from YukkiMusic.utils.database import get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("YukkiMusic").error(
            "WTF Baby, Atleast add a pyrogram string, How Cheap !"
        )
        return
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("YukkiMusic.plugins" + all_module)
    LOGGER("Yukkimusic.plugins").info(
        "Successfully Imported Modules "
    )
    await userbot.start()
    await Yukki.start()
    try:
        await Yukki.stream_call(
            "https://telegra.ph/file/b511cf0605c7fde1e9a49.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("YukkiMusic").error(
            "[ERROR] - \n\nHey Baby, firstly open telegram and turn on voice chat in Logger Group else fu*k off. If you ever ended voice chat in log group i will stop working and users will fu*k you up."
        )
        sys.exit()
    except:
        pass
    await Yukki.decorators()
    LOGGER("YukkiMusic").info("Music Bot Successfully Started Baby. Enjoy !")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("YukkiMusic").info("Stopping Music Bot. Fu*k Off !")
