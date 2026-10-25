import json
import telebot

TOKEN = "7275178891:AAFTCA9Wd5-5LUnOBonUi51NE4glDe5pRH8"
bot = telebot.TeleBot(TOKEN)

def handler(event, context):
    try:
        # التأكد من أن الطلب هو POST قادم من تلغرام
        if event.get("httpMethod") == "POST":
            body = event.get("body")
            if body:
                json_string = body
                update = telebot.types.Update.de_json(json_string)
                bot.process_new_updates([update])

        return {
            "statusCode": 200,
            "body": json.dumps({"status": "success"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
