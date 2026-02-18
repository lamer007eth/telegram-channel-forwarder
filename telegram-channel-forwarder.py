import asyncio
import os
from datetime import datetime
from telethon import TelegramClient, events
from dotenv import load_dotenv

load_dotenv(".env")

# =========================
# ENV
# =========================
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

TARGET_CHANNEL = os.getenv("TARGET_CHANNEL")

FULL_FORWARD_CHANNELS = os.getenv("FULL_FORWARD_CHANNELS", "")
FILTERED_CHANNEL = os.getenv("FILTERED_CHANNEL")

RECONNECT_DELAY = int(os.getenv("RECONNECT_DELAY", "5"))

SESSION_NAME = os.getenv("SESSION_NAME", "forwarder_session")

# Convert CSV → list
FULL_FORWARD_CHANNELS = [
    ch.strip() for ch in FULL_FORWARD_CHANNELS.split(",") if ch.strip()
]

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)


# =========================
# FILTER LOGIC
# =========================
def passes_filter(chat_username: str, text: str) -> bool:
    """
    Custom filter for selected channel
    """
    if chat_username == FILTERED_CHANNEL:
        if "Collection Link: https://t.me/sticker_bot/" not in text:
            return False
    return True


# =========================
# HANDLER
# =========================
@client.on(events.NewMessage(chats=FULL_FORWARD_CHANNELS + [FILTERED_CHANNEL]))
async def forward_handler(event):
    chat = await event.get_chat()
    chat_username = chat.username or "unknown"
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    text = event.message.message or ""

    if not passes_filter(chat_username, text):
        print(f"[{timestamp}] ⚠️ Skipped @{chat_username} (filter mismatch)")
        return

    try:
        await client.send_message(TARGET_CHANNEL, event.message)
        print(f"[{timestamp}] 📬 Forwarded @{chat_username} → @{TARGET_CHANNEL}")
    except Exception as e:
        print(f"[{timestamp}] ❌ Forward error: {e}")


# =========================
# MAIN LOOP
# =========================
async def main():
    while True:
        try:
            print("🔄 Forwarder started. Listening for new messages...")
            await client.start()
            await client.run_until_disconnected()
        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{timestamp}] ❌ Error: {e}. Reconnecting in {RECONNECT_DELAY}s...")
            await asyncio.sleep(RECONNECT_DELAY)


if __name__ == "__main__":
    asyncio.run(main())
