from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""مرحبا, انا 𝙎𝙉𝙀𝙆𝙍𝙎 🍫

انا اعمل في المجموعات لايمكن تشغيلي في الخاص 🎼
قم برفعي مشرف في مجموعتك 
قم باضافه الحساب المساعد  [𝙎𝙉𝙀𝙆𝙍𝙎 🍫](https://t.me/SnekrsVoice).
ارسل اغنيه بصمه او mp3 او رابط من اليوتيوب 
قم بالرد على الرابط او البصمه وارسل /play
تستطيع البحث في اليوتيوب باستخدام البوت
مثال
@hmh_bbot كاظم الساهر
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⌁︙ للمساعده ︙⌁", url="https://t.me/hhmhhh")
                  ],[
                    InlineKeyboardButton(
                        "⌁︙ قناة تمبلر ︙⌁", url="https://t.me/O9oOoO"
                    ),
                    InlineKeyboardButton(
                        "⌁︙ قناة للمطورين ︙⌁", url="https://t.me/CQCQQ"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "⌁︙ اضافتي الى مجموعة ︙⌁", url="https://t.me/hmh_bbot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""Group Music Player Online ✅""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⌁︙ متحركات اطفال ︙⌁", url="https://t.me/z44z4")
                ]
            ]
        )
   )
