import asyncio
import json
import os
from telegram.ext import ApplicationBuilder, CommandHandler
from utils.binance_fetch import fetch_price
from utils.grafico import gerar_grafico
from utils.ai_interpreter import interpretar_mensagem
from telegram import Update
from telegram.ext import ContextTypes

with open("config.json") as f:
    config = json.load(f)
TEMPO_ANALISE = config.get("tempo_execucao_minutos", 15)

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot Sahara Monitor ativo. Use /tempo <minutos> para alterar o intervalo.")

async def tempo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        novo_tempo = int(context.args[0])
        config["tempo_execucao_minutos"] = novo_tempo
        with open("config.json", "w") as f:
            json.dump(config, f)
        await update.message.reply_text(f"Novo tempo definido: {novo_tempo} minutos.")
    except:
        await update.message.reply_text("Uso correto: /tempo 10")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("tempo", tempo))
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
