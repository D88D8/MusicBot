from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**مرحبا, انا **𝗠𝗨𝗦𝗜𝗖 𝗦𝗧𝗢𝗥𝗠** 🎵

انا اعمل في المجموعات لايمكن تشغيلي في الخاص 🎼
قم برفعي مشرف في مجموعتك 
قم باضافه الحساب المساعد  [𝗠𝗨𝗦𝗜𝗖 𝗦𝗧𝗢𝗥𝗠](https://t.me/MUSIC_VOICEY).
ارسل اغنيه بصمه او mp3 او رابط من اليوتيوب 
قم بالرد على الرابط او البصمه وارسل /play
تستطيع البحث في اليوتيوب باستخدام البوت
مثال
@MusiVchatBot كاظم الساهر**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 للمساعده 🛠", url="https://t.me/hhmhhh")
                  ],[
                    InlineKeyboardButton(
                        "💬 مجموعه", url="https://t.me/in_arrray"
                    ),
                    InlineKeyboardButton(
                        "🔊 القناة", url="https://t.me/CQCQQ"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ اضافه الى مجموعتك ➕", url="https://t.me/zK_GvCBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 قناتي", url="https://t.me/CQCQQ")
                ]
            ]
        )
   )


