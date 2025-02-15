#!/usr/bin/env python3
# This is bot coded by AbhijithNT and used for educational purposes only
# https://github.com/AbhijithNT
# Copyright ABHIJITH N T
# Thank you https://github.com/pyrogram/pyrogram




import os
import time
from bot import LOGGER
from ..display import progress
from pyrogram.errors import FloodWait
from ..upload_servers import fileIO, transferSH, filedropper, anonymFiles

async def fileDownload(client, bot):
    file_path = ''
    now = time.time()
    upload_server = bot.data
    user_message = await client.edit_message_text(
        chat_id=bot.from_user.id,
        message_id=bot.message.message_id,
        text="processing your request...please wait",
    )

    user_progress = user_message

    try:
        file_path = await client.download_media(
            message=user_message.reply_to_message,
            progress=progress,
            progress_args=(
                "Downloading...",
                user_progress,
                now
            )
        )
    except FloodWait as e:
        LOGGER.info(f"{e}")
        print(time.sleep(e.x))


    if upload_server == "File.io":
        await fileIO(file_path, client, user_progress, now)
    if upload_server == "transfersh":
        await transferSH(file_path, client, user_progress, now)
    if upload_server == "filedropper":
        await filedropper(file_path, client, user_progress, now)
    if upload_server == "anonymfiles":
        await anonymFiles(file_path, client, user_progress, now)


    try:
        os.remove(file_path)
        LOGGER.info(f"{file_path}")
    except OSError as error:
        LOGGER.info(f"Error: {error.filename} - {error.strerror}.")
        print("Error: %s - %s." % (error.filename, error.strerror))
