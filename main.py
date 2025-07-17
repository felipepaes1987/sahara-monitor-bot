import asyncio
import logging
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update
import json
from utils.binance_fetch import fetch_price
from utils.grafico import gerar_grafico
from utils.ai_interpreter import interpretar_situacao

with open("config.json") as f:
    config = json.load(f)

TOKEN = config["TELEGRAM_TOKEN"]
logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Sou o bot de monitoramento do token SAHARA.")

async def alerta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    preco, volume = fetch_price()
    grafico_path = gerar_grafico(preco)
    interpretacao = interpretar_situacao(preco, volume)
    await update.message.reply_photo(photo=open(grafico_path, "rb"), caption=interpretacao)

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("alerta", alerta))
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
