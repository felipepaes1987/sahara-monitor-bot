import asyncio
from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from utils.grafico import gerar_grafico
from utils.ai_interpreter import interpretar_contexto
from utils.binance_fetch import buscar_dados_binance
import json
import os

with open("config.json", "r") as f:
    config = json.load(f)

TOKEN = config["telegram_token"]
CHAT_ID = config["chat_id"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🤖 Bot Sahara Monitor ativo!")

async def enviar_analise(context: ContextTypes.DEFAULT_TYPE):
    dados = buscar_dados_binance()
    interpretacao = interpretar_contexto(dados)
    imagem = gerar_grafico(dados)

    with open(imagem, "rb") as img:
        await context.bot.send_photo(chat_id=CHAT_ID, photo=InputFile(img),
                                     caption=f"📈 Análise Sahara\n\n{interpretacao}")

async def agendar_tarefas(app):
    from apscheduler.schedulers.asyncio import AsyncIOScheduler
    scheduler = AsyncIOScheduler()
    scheduler.add_job(enviar_analise, "interval", minutes=config["intervalo_minutos"], args=[app.bot])
    scheduler.start()

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    await agendar_tarefas(app)
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())