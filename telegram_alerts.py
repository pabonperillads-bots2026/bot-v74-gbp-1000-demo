# telegram_alerts.py - NIVEL 3 DANNY - Avisa a tu celular
import os, requests

def enviar_telegram(mensaje):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    
    if not token or not chat_id:
        print("Telegram: FALTA SECRETO - Configura en GitHub Secrets")
        return False
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": f"🤖 BOT V7.4 GBP DANNY\n{mensaje}", "parse_mode": "Markdown"}
    
    try:
        r = requests.post(url, data=data, timeout=10)
        if r.status_code == 200:
            print(f"✅ Telegram OK: {mensaje[:30]}")
            return True
        else:
            print(f"❌ Telegram error: {r.text}")
            return False
    except Exception as e:
        print(f"❌ Telegram exception: {e}")
        return False

if __name__ == "__main__":
    enviar_telegram("Prueba PRO+ 1000 GBP Frankfurt - Bot activo")
