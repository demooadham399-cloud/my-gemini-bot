import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# بياناتك الشغالة تماماً
API_KEY = "AIzaSyD_2jkUhUOdygtkjVbF_Q_UdhAg2E_Ymyk"
TOKEN = "8566545568:AAF0hCMFB8HkZBSwCQFxo2T9GCbe8LCJeaQ"

async def ai_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
    try:
        payload = {"contents": [{"parts": [{"text": user_text}]}]}
        response = requests.post(url, json=payload, timeout=20)
        result = response.json()
        if 'candidates' in result:
            reply = result['candidates'][0]['content']['parts'][0]['text']
            await update.message.reply_text(reply)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), ai_handler))
    app.run_polling()
