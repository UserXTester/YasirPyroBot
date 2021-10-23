from pyrogram import Client, filters
from bot import app

@app.on_message(filters.command(["start"]))
async def start(client, message):
    await message.reply_text(
        text=f"Hai {message.from_user.mention}"
)
