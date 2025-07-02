from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from binance.client import Client
import os

# Ganti dengan API bot Telegram Anda
TELEGRAM_BOT_TOKEN = '7749381087:AAG7CgTC853g5AendRr3wz68yHaVWDaYS34'

# Ganti dengan API Binance Anda (bisa pakai kosong untuk hanya akses publik)
binance_client = Client(api_key='', api_secret='')

# Fungsi ambil harga
async def get_price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        symbol = 'BTCUSDT'  # Bisa disesuaikan atau dikirim via argumen
        ticker = binance_client.get_symbol_ticker(symbol=symbol)
        price = ticker['price']
        await update.message.reply_text(f"Harga {symbol}: ${price}")
    except Exception as e:
        await update.message.reply_text("Gagal mengambil data harga.")

# Fungsi start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Kirim /price untuk melihat harga BTC/USDT.")

# Inisialisasi bot
app = ApplicationBuilder().token(7749381087:AAG7CgTC853g5AendRr3wz68yHaVWDaYS34).build()

# Handler
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", get_price))

# Jalankan bot
app.run_polling()
