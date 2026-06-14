'''from fastapi import FastAPI, Request
from telegram import Bot
from pydantic import BaseModel
from dotenv import load_dotenv

import os

load_dotenv()

app = FastAPI()

TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TOKEN)


class Message(BaseModel):
    chat_id: int
    text: str


@app.get("/")
def home():
    return {
        "status": "online"
    }


@app.post("/send")
async def send(msg: Message):

    await bot.send_message(
        chat_id=msg.chat_id,
        text=msg.text
    )

    return {
        "ok": True
    }

@app.post("/webhook")
async def webhook(request: Request):

    data = await request.json()

    print("Recebido:")
    print(data)

    message = data.get("message")

    if message:

        texto = message.get("text")

        chat_id = message.get("chat", {}).get("id")

        print("Chat:", chat_id)
        print("Texto:", texto)

    return {
        "ok": True
    }'''