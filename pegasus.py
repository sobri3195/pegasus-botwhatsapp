import os
import requests
import json
import datetime

# Set your credentials
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

# Set your bot's webhook URL
webhook_url = "https://api.whatsapp.com/v2/webhooks/register"

# Create a new WhatsApp Bot
bot = WhatsAppBot(api_key, api_secret)

# Set the bot's webhook
bot.set_webhook(webhook_url)

# Define the bot's handlers
@bot.on("message")
def handle_message(message):

    # Get the message's text
    text = message.get("text")

    # Handle the message
    if text == "Lihat Poliklinik":
        bot.send_message(message.get("from"), get_poliklinik())
    elif text == "Lihat Jadwal Poliklinik Besok":
        bot.send_message(message.get("from"), get_jadwal_poliklinik_besok())
    elif text == "Pendaftaran Poliklinik Pasien Lama/Sudah Memiliki Nomor Rekam Medis (H-1)":
        bot.send_message(message.get("from"), get_pendaftaran_poliklinik_pasien_lama())
    elif text == "Pendaftaran Poliklinik Pasien Baru":
        bot.send_message(message.get("from"), get_pendaftaran_poliklinik_pasien_baru())
    elif text == "Atur/Ganti Sandi Sidarling Website":
        bot.send_message(message.get("from"), get_atur_ganti_sandi_sidarling_website())
    elif text == "Lihat Sandi Sidarling Website":
        bot.send_message(message.get("from"), get_lihat_sandi_sidarling_website())
    elif text == "Lihat Nomor RM (Rekam Medis) Pasien":
        bot.send_message(message.get("from"), get_lihat_nomor_rm_pasien())
    elif text == "Lihat Nomor Antrian Apotek Poli":
        bot.send_message(message.get("from"), get_lihat_nomor_antrian_apotek_poli())

# Start the bot
bot.start()
