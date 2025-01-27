from asyncio.queues import QueueEmpty

from pyrogram import Client
from pyrogram.types import Message

import callsmusic

from config import BOT_NAME as BN
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only


@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'paused'
    ):
        await message.reply_text(f"**@Z44Z4\n لم يتم تشغيل اي اغنيه ❌\n قم بارسال اغنيه او رابط \n بعدها قم بالرد عليها وارسال /play ♻️**")
    else:
        callsmusic.pytgcalls.pause_stream(message.chat.id)
        await message.reply_text(f"**@Z44Z4\n تم ايقاف الاغنيه ✅**")


@Client.on_message(command("resume") & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'playing'
    ):
        await message.reply_text(f"**@Z44Z4\n لاتوجد اغنيه متوقفه 🎶**")
    else:
        callsmusic.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text(f"**@Z44Z4 \n تم استئناف تشغيل الاغنيه ♻️**")


@Client.on_message(command("stop") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text(f"**@Z44Z4\n لاتوجد اغنيه قيد التشغيل لايقافها ❌**")
    else:
        try:
            callsmusic.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text(f"**@Z44Z4 \n تم ايقاف الاغنيه الحاليه ✅**")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text(f"**@Z44Z4 \n لاتوجد اغنيه قيد التشغيل 🎶**")
    else:
        callsmusic.queues.task_done(message.chat.id)

        if callsmusic.queues.is_empty(message.chat.id):
            callsmusic.pytgcalls.leave_group_call(message.chat.id)
        else:
            callsmusic.pytgcalls.change_stream(
                message.chat.id,
                callsmusic.queues.get(message.chat.id)["file_path"]
            )

        await message.reply_text(f"**@Z44Z4 \n تم تخطي الاغنيه الحاليه ♻️**")
