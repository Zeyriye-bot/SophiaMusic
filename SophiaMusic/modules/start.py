from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""Hi there,👋 {message.from_user.first_name}!
\nThis is 𝕆𝕤𝕞𝕒𝕟𝕚 𝔹𝕠𝕥 ℂ𝕖𝕟𝕥𝕖𝕣.
I play music on Telegram's Voice Chats.
\nFo More Help Use Buttons Below:
 """,
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "☞︎︎︎ ℂ𝕠𝕞𝕞𝕒𝕟𝕕 ☜︎︎︎", url="https://telegra.ph/Mss-Rosan-03-24")
                  ],[
                    InlineKeyboardButton(
                        "☞︎︎︎ 𝕋𝕖𝕒𝕞 𝕆𝕤𝕞𝕒𝕟𝕚 ☜︎︎︎", url="https://t.me/teamosmani"
                    ),
                    InlineKeyboardButton(
                        "☞︎︎︎ 𝕤𝕦𝕡𝕡𝕠𝕣𝕥 ☜︎︎", url="https://t.me/osmanigroupbot"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url="https://t.me/CenterOsmaniBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""* Osmani Music Bot is alive.*""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Updates Channel", url="https://t.me/osmanibots")
                ]
            ]
        )
   )


