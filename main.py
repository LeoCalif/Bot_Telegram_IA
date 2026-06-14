import telebot
from dotenv import load_dotenv
import os
import requests
import json


load_dotenv()

TOKEN_TELEGRAM = os.getenv("TELEGRAM_TOKEN")
TOKEN_OPENROUTER = os.getenv("OPENAI_API_KEY")

if not TOKEN_TELEGRAM:
    raise ValueError("Token Telegram não encontrado")
    exit()

if not TOKEN_OPENROUTER :
    raise ValueError("Token OpenRouter não encontrado")
    exit()
try:
    bot = telebot.TeleBot(TOKEN_TELEGRAM)

    @bot.message_handler(commands=['start', 'help'])
    def mensagem_boas_vindas(mensagem):
        bot.reply_to(mensagem, "Bem vindo")

    @bot.message_handler(func=lambda m: True)
    def responder_tudo(mensagem):
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": "Bearer " + TOKEN_OPENROUTER,
                "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional. Site URL for rankings on openrouter.ai.
                "X-OpenRouter-Title": "<YOUR_SITE_NAME>",  # Optional. Site title for rankings on openrouter.ai.
            },
            data=json.dumps({
                "model": "openai/gpt-oss-120b:free",
                "messages": [
                    {
                        "role": "user",
                        "content": mensagem.text
                    }
                ]
            })
        )
        dados = response.json()
        if "choices" in dados:
            texto_da_ia = dados["choices"][0]["message"]["content"]
            bot.reply_to(mensagem, texto_da_ia )
        else:
            print ("Erro na resposta", dados)


    print("Bot rodando...")
    bot.polling()

except Exception as e:
    print("Erro:", e)