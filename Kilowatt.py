import requests
import time

# Telegram-Konfiguration
BOT_TOKEN = "7208495645:AAGCcpceJD5UVSU4m8o5W3evzAtLthreWX0"
CHAT_ID = "6603501987"

# Steam-Konfiguration
ITEM_NAME = "Kilowatt Case"
STEAM_MARKET_URL = (
    f"https://steamcommunity.com/market/priceoverview/?country=DE&currency=3&appid=730&market_hash_name={ITEM_NAME.replace(' ', '%20')}"
)

# Preisschwelle
TARGET_PRICE = 0.60

def get_kilowatt_price():
    try:
        response = requests.get(STEAM_MARKET_URL)
        data = response.json()
        if "lowest_price" in data:
            price_str = data["lowest_price"].replace("€", "").replace(",", ".").strip()
            return float(price_str)
    except Exception as e:
        print("Fehler beim Preisabruf:", e)
    return None

def send_telegram_message(text):
    # Hier Variable BOT_TOKEN und CHAT_ID verwenden
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    try:
        r = requests.post(url, data=payload)
        print("Nachricht überbracht:", r.status_code)
    except Exception as e:
        print("Telegram-Fehler:", e)

def main():
    price = get_kilowatt_price()
    print("Aktueller Preis:", price)
    if price and price >= TARGET_PRICE:
        send_telegram_message(f"🚨 Kilowatt Case Preis: {price:.2f} € – JTo the Mooooooooon!!!!!!!")
    else:
        print("No money :(")

if __name__ == "__main__":
    main()
